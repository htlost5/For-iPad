from PIL import Image, ImageDraw, ImageFont, ImageSequence
import numpy as np

# Load the image generated by DALL-E
base_image_path = "/home/codespace/For-iPad/gif/Unknown 2.jpeg"
base_img = Image.open(base_image_path)

# Convert the base image to RGB mode
base_img = base_img.convert("RGB")

# Prepare to create rotating letters around the circle
frames = []
n_frames = 36  # Number of frames for smooth rotation
center_x, center_y = base_img.width // 2, base_img.height // 2
radius = 300  # Approximate distance from center for the letters
letters = "htlost5"
font_size = 40

# Create the font (using a default font)
try:
    font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", font_size)
except IOError:
    font = ImageFont.load_default()

# Generate rotating frames
for i in range(n_frames):
    frame = base_img.copy()
    draw = ImageDraw.Draw(frame)
    
    # Calculate the angle for each letter
    for j, letter in enumerate(letters):
        angle = 2 * np.pi * (i + j) / n_frames  # Rotation angle for each letter
        x = int(center_x + radius * np.cos(angle))
        y = int(center_y + radius * np.sin(angle))
        
        # Draw each letter at the calculated position
        draw.text((x, y), letter, font=font, fill=(255, 255, 255))
    
    # Append the frame to the frames list
    frames.append(frame)

# Save the frames as an animated GIF
output_gif_path = "/home/codespace/For-iPad/gif/rotating_letters_around_circle.gif"
frames[0].save(output_gif_path, save_all=True, append_images=frames[1:], duration=100, loop=0)

print(output_gif_path)