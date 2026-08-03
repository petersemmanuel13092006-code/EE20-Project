# EE20-Project
GET 324 mini project for group EE20
Banana Ripeness Detection
Overview

Banana Ripeness Detection is a deep learning-powered web application built with Streamlit and TensorFlow. The application classifies an uploaded banana image as either Ripe or Unripe.

To improve prediction reliability, the application first validates that the uploaded image actually contains a banana using a pre-trained MobileNetV2 model trained on the ImageNet dataset. Only images identified as bananas are passed to the custom ripeness classification model.

Features
Upload banana images (.jpg, .jpeg, .png)
Automatic banana image validation using MobileNetV2
Classifies bananas as:
Ripe
Unripe
Displays prediction confidence
Warns users when predictions are uncertain
Interactive web interface built with Streamlit
Project Structure
project/
│
├── app.py                    # Main Streamlit application
├── banana_model.keras        # Trained banana ripeness classification model
├── requirements.txt          # Python dependencies
└── README.md                 # Project documentation

How It Works
1. Upload an Image

Users upload a banana image through the Streamlit web interface.

Supported formats:

JPG
JPEG
PNG
2. Banana Validation

Before predicting ripeness, the application verifies that the uploaded image contains a banana.

The validation uses the pre-trained MobileNetV2 model with ImageNet weights.

The model checks its top predictions for labels containing:

banana
fruit
plantain

If no valid banana-related label is detected, the application displays:

This doesn't look like a banana.
Please upload a clearer photo of a banana.


This prevents incorrect predictions on unrelated images.

3. Image Preprocessing

If the image passes validation, it is:

Converted to RGB
Resized to 224 × 224
Normalized by scaling pixel values to the range [0,1]
Converted into a batch before inference
4. Ripeness Prediction

The processed image is passed to the custom TensorFlow model.

Possible predictions:

Ripe
Unripe

The application also displays the prediction confidence.

5. Uncertain Predictions

If the prediction probability falls between 0.40 and 0.60, the application considers the result uncertain and prompts the user to upload a clearer image.

Example:

Uncertain prediction (confidence: 0.52).
Try a clearer image.

Technologies Used
Python
Streamlit
TensorFlow
Keras
MobileNetV2 (ImageNet)
NumPy
Pillow (PIL)
Installation
Clone the repository
git clone https://github.com/yourusername/banana-ripeness-detection.git

cd banana-ripeness-detection

Install dependencies
pip install -r requirements.txt

Run the application
streamlit run app.py

Required Files

Ensure the following file is present in the project directory:

banana_model.keras

Without this trained model, the application cannot perform ripeness prediction.

Example Workflow
Launch the application.
Upload a banana image.
MobileNetV2 verifies that the image contains a banana.
If validation succeeds, the custom model predicts whether the banana is Ripe or Unripe.
The predicted class and confidence score are displayed.
Future Improvements
Detect multiple ripeness stages (Green, Turning, Yellow, Ripe, Overripe)
Support batch image uploads
Display Grad-CAM heatmaps for model interpretability
Mobile-responsive interface
REST API for integration with external systems
Cloud deployment using Streamlit Community Cloud or Docker
Prediction history and analytics dashboard
License

This project is intended for educational and research purposes. You are free to modify and extend it to suit your needs.

Author
Reg number: 23/EG/EE/019
Developed as a deep learning application for automated banana ripeness classification using TensorFlow, MobileNetV2, and Streamlit.
