from PIL import Image

def create_tracker_pixel():
    # Create a new 1x1 image with RGBA mode (A for alpha transparency)
    img = Image.new("RGBA", (1, 1), (0, 0, 0, 0))  # Fully transparent pixel (0, 0, 0, 0)

    # Save the image as a .gif file (supports transparency)
    img.save("1x1-transparent.gif", "GIF")

# Call the function to create the pixel
create_tracker_pixel()
