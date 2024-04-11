import streamlit as st
import os
from PIL import Image


def display_images(folder_path):
    """Recursively display images in all subfolders."""
    # Initialize a list to hold image paths and captions
    images_to_display = []

    for item in os.listdir(folder_path):
        full_path = os.path.join(folder_path, item)

        if os.path.isdir(full_path):
            # If the item is a folder, dive into it recursively
            display_images(full_path)
        elif item.lower().endswith(('.png', '.jpg', '.jpeg')):
            # If the item is an image, add it to the list
            images_to_display.append((full_path, item))

    # Display images in batches of 4
    for i in range(0, len(images_to_display), 4):
        # Create a row with 4 columns
        cols = st.columns(4)
        for col, img_info in zip(cols, images_to_display[i:i + 4]):
            # Open and display each image in its respective column
            image_path, caption = img_info
            image = Image.open(image_path)
            col.image(image, caption=caption, use_column_width=True)


# Title of your app
st.title('Pokemon Image Gallery')

# Base directory where your images are stored
base_folder = '/usr/src/scrapper/data'

# Start the image display process from the base folder
display_images(base_folder)
