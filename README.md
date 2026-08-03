# EE20-Project
GET 324 mini project for group EE20
Banana Ripeness Detection
Overview

Banana Ripeness Detection is a web application built with Streamlit and TensorFlow that classifies bananas as Ripe or Unripe from uploaded images. Before making a prediction, the application validates that the uploaded image contains a banana using the pre-trained MobileNetV2 model, helping to improve the reliability of the results.

Features
Upload banana images in JPG, JPEG, or PNG format.
Automatically validates that the uploaded image contains a banana.
Predicts whether the banana is Ripe or Unripe.
Displays prediction confidence.
Detects uncertain predictions and prompts users to upload a clearer image.
User-friendly web interface powered by Streamlit.
Technologies Used
Python 3.x
Streamlit
TensorFlow / Keras
MobileNetV2 (ImageNet)
NumPy
Pillow (PIL)
Project Structure
project/
│
├── app.py                  # Main Streamlit application
├── banana_model.keras      # Trained banana ripeness model
├── requirements.txt        # Python dependencies
└── README.md               # Project documentation

Installation
Clone the repository.
git clone https://github.com/yourusername/banana-ripeness-detection.git

Navigate to the project directory.
cd banana-ripeness-detection

Install the required packages.
pip install -r requirements.txt

Running the Application

Start the Streamlit application with:

streamlit run app.py


The application will open in your default web browser.

How It Works
The user uploads an image of a banana.
The image is resized and preprocessed.
A pre-trained MobileNetV2 model verifies that the uploaded image contains a banana.
If the image is valid, it is passed to the custom-trained banana ripeness model.
The model predicts whether the banana is:
Ripe
Unripe
The prediction confidence is displayed.
If the prediction confidence falls within an uncertain range (0.40–0.60), the application asks the user to upload a clearer image.
Model Information
Validation Model
Architecture: MobileNetV2
Weights: ImageNet
Purpose: Verify that the uploaded image is a banana before classification.
Classification Model
File: banana_model.keras
Purpose: Predict banana ripeness.
Output Classes:
Ripe
Unripe
Supported Image Formats
JPG
JPEG
PNG
Dependencies
streamlit
tensorflow
numpy
pillow

Future Improvements
Support multiple ripeness stages (e.g., Green, Turning, Ripe, Overripe).
Display prediction probabilities for all classes.
Improve banana validation with a custom object detection model.
Enable batch image processing.
Deploy the application to a cloud platform such as Streamlit Community Cloud.
License
Reg number: 23/EG/EE/089
This project is available under the MIT License. You are free to use, modify, and distribute it in accordance with the license terms.
Reg number: 
Acknowledgements
TensorFlow and Keras for deep learning tools.
Streamlit for the web application framework.
MobileNetV2 for pre-trained image classification on the ImageNet dataset.
