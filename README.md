# EE20-Project
GET 324 mini project for group EE20


# Banana Ripeness Detection

## Overview
Banana Ripeness Detection is a simple web app built with Streamlit that lets a user upload a photo of a banana and get an instant prediction of whether it is **Ripe** or **Unripe**. The app uses a custom-trained Keras image classification model, combined with a MobileNetV2-based validation step that checks the uploaded image actually contains a banana before running the ripeness prediction.

## Features
- Upload a banana image (`.jpg`, `.jpeg`, `.png`) through a simple web interface
- Automatic validation step using MobileNetV2 (ImageNet weights) to confirm the uploaded image is actually a banana/fruit before classifying
- Rejects non-banana images with a clear error message
- Predicts **Ripe** or **Unripe** using a custom-trained Keras model
- Displays prediction confidence as a percentage
- Flags uncertain predictions (confidence between 0.4–0.6) and asks the user to try a clearer image
- Cached model loading (`@st.cache_resource`) for faster repeated predictions

## Technologies Used
- Python
- Streamlit – web app interface
- TensorFlow / Keras – model loading and inference
- MobileNetV2 (pretrained on ImageNet) – used for input validation
- NumPy – array/image processing
- Pillow (PIL) – image loading and preprocessing


Reg Number: 23/EG/EE/069
