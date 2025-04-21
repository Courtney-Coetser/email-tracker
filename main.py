from flask import Flask, request, send_file, render_template_string
import os

app = Flask(__name__)

# In-memory storage for stats (can be replaced with a database)
stats = {
    "total_opens": 0,
    "unique_ips": set(),
    "user_agents": {}
}

# Route to show stats on the main page
@app.route('/')
def dashboard():
    total_opens = stats["total_opens"]
    unique_ips = len(stats["unique_ips"])
    user_agents = stats["user_agents"]

    dashboard_html = """
    <html>
    <head>
        <title>Email Tracker Dashboard</title>
    </head>
    <body>
        <h1>Email Tracker Dashboard</h1>
        <p><strong>Total Email Opens:</strong> {{ total_opens }}</p>
        <p><strong>Unique IPs:</strong> {{ unique_ips }}</p>
        <h3>User Agents:</h3>
        <ul>
        {% for user_agent, count in user_agents.items() %}
            <li>{{ user_agent }}: {{ count }}</li>
        {% endfor %}
        </ul>
        <p><a href="/track_pixel">Track Pixel Link</a></p>
    </body>
    </html>
    """

    return render_template_string(dashboard_html, total_opens=total_opens, unique_ips=unique_ips, user_agents=user_agents)

# A simple route to track email opens
@app.route('/track_pixel', methods=['GET'])
def track_email_open():
    # Here we log the open event: increment total opens, track unique IPs and user agents.
    user_ip = request.remote_addr
    user_agent = request.headers.get('User-Agent')

    # Update the stats
    stats["total_opens"] += 1
    stats["unique_ips"].add(user_ip)

    if user_agent in stats["user_agents"]:
        stats["user_agents"][user_agent] += 1
    else:
        stats["user_agents"][user_agent] = 1

    # Print for debugging (you can remove or replace with logging in production)
    print(f"Email opened by {user_ip}, User-Agent: {user_agent}")

    # Return a 1x1 transparent pixel (GIF) as a response
    pixel_path = os.path.join(os.path.dirname(__file__), "1x1-transparent.gif")
    return send_file(pixel_path, mimetype='image/gif')

if __name__ == '__main__':
    app.run(debug=True)
