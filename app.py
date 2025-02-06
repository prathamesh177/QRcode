import streamlit as st
import cv2
from pyzbar.pyzbar import decode
import numpy as np
from PIL import Image

# Function to decode the barcode
def decode_barcode(image):
    decoded_objects = decode(image)
    if decoded_objects:
        return decoded_objects[0].data.decode('utf-8')
    return "No barcode detected"

# Streamlit app
def app():
    st.title("Barcode Scanner")

    # Open the camera
    camera = st.camera_input("Capture Barcode")

    if camera is not None:
        # Convert the image to OpenCV format
        img = Image.open(camera)
        img_array = np.array(img)

        # Decode the barcode
        barcode_info = decode_barcode(img_array)

        # Display the barcode image
        st.image(img, caption="Captured Image", use_column_width=True)

        # Display the barcode information
        st.write(f"Barcode Information: {barcode_info}")

if __name__ == "__main__":
    app()
