# EE20-Project
GET 324 mini project for group EE20
🍌 Banana Ripeness Detection

A Streamlit web application that uses a deep learning model to classify bananas as Ripe or Unripe from an uploaded image. Before classification, the application validates that the uploaded image actually contains a banana using the pre-trained MobileNetV2 ImageNet model.

Features
Upload banana images (.jpg, .jpeg, .png)
Validates whether the uploaded image contains a banana
Predicts whether the banana is:
Ripe
Unripe
Displays prediction confidence
Warns the user when the model is uncertain
Simple and interactive Streamlit interface
Project Structure
banana-ripeness-detection/
│
├── app.py                  # Streamlit application
├── banana_model.keras      # Trained banana classification model
├── requirements.txt        # Project dependencies
├── README.md               # Project documentation

Requirements
Python 3.9 or later
TensorFlow
Streamlit
NumPy
Pillow

Install the required packages:

pip install -r requirements.txt


Or install them manually:

pip install streamlit tensorflow numpy pillow

Running the Application

Start the Streamlit app using:

streamlit run app.py


The application will open in your default web browser.

How It Works
Step 1: Upload an Image

The user uploads an image containing a banana.

Step 2: Banana Validation

The uploaded image is first processed by the pre-trained MobileNetV2 model trained on the ImageNet dataset.

The application checks the top predictions for labels such as:

banana
plantain
fruit

If no banana-related label is detected, the application displays an error asking the user to upload a clearer banana image.

Step 3: Ripeness Classification

If the image passes validation:

The image is resized to 224 × 224 pixels.
Pixel values are normalized.
The image is passed to the custom-trained model (banana_model.keras).
The model predicts whether the banana is:
Ripe
Unripe
Step 4: Confidence Score

The application displays:

Predicted class
Prediction confidence

If the prediction probability falls between 0.40 and 0.60, the application considers the prediction uncertain and recommends uploading a clearer image.

Model Information
Validation Model
MobileNetV2
Pre-trained on ImageNet
Used only to verify that the uploaded image contains a banana
Classification Model
Custom TensorFlow/Keras model
Saved as:
banana_model.keras


Output classes:

Prediction	Meaning
0	Ripe
1	Unripe

Decision threshold:

Prediction > 0.5 → Unripe
Prediction ≤ 0.5 → Ripe
Supported Image Formats
JPG
JPEG
PNG
Example Workflow
Launch the application.
Upload a banana image.
The application validates the image.
If a banana is detected, the ripeness model runs.
The prediction and confidence score are displayed.
Future Improvements
Support multiple banana varieties.
Add a third "Overripe" class.
Display Grad-CAM heatmaps for model explainability.
Improve confidence calibration.
Enable webcam image capture.
Deploy the application on Streamlit Community Cloud or another cloud platform.
Technologies Used
Python
Streamlit
TensorFlow / Keras
MobileNetV2
NumPy
Pillow
Author
Reg Number: 24/EG/EE/369
Developed as a deep learning application for automated banana ripeness classification using TensorFlow and Streamlit.
