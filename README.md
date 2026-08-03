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
=======
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
=======

# 🍌 Banana Ripeness Detection

A Streamlit web application that uses a TensorFlow deep learning model to classify whether a banana is **Ripe** or **Unripe** from an uploaded image.

Before making a prediction, the application validates that the uploaded image actually contains a banana using the pre-trained **MobileNetV2** ImageNet model.

---

## Features

- Upload banana images in JPG, JPEG, or PNG format.
- Validates that the uploaded image contains a banana before classification.
- Predicts whether the banana is:
  - Ripe
  - Unripe
- Displays prediction confidence.
- Warns the user when the model is uncertain.
- Simple and interactive Streamlit interface.

---

## Project Structure

```
project/
│
├── app.py
├── banana_model.keras
├── requirements.txt
└── README.md
```

---

## Requirements

- Python 3.9 or later
- TensorFlow
- Streamlit
- NumPy
- Pillow

Install all dependencies with:

```bash
pip install -r requirements.txt
```

---

## Running the Application

Start the Streamlit application with:

```bash
streamlit run app.py
```

The application will open automatically in your web browser.

---

## How It Works

### Step 1: Upload an Image

The user uploads an image of a banana in one of the supported formats:

- JPG
- JPEG
- PNG

---

### Step 2: Banana Validation

The uploaded image is first processed using the pre-trained **MobileNetV2** model with ImageNet weights.

The application checks the top predictions returned by MobileNetV2 for labels containing:

- banana
- fruit
- plantain

If none of these labels are detected with sufficient confidence, the application displays:

> "This doesn't look like a banana. Please upload a clearer photo of a banana."

This prevents the custom model from making predictions on unrelated images.

---

### Step 3: Ripeness Classification

If the image passes validation:

- The image is resized to **224 × 224**
- Pixel values are normalized to the range **0–1**
- The processed image is passed to the custom TensorFlow model (`banana_model.keras`)

The model outputs a probability used to determine the final class.

Prediction logic:

- Probability > 0.5 → **Unripe**
- Probability ≤ 0.5 → **Ripe**

---

### Step 4: Confidence Check

To avoid unreliable predictions, the application checks whether the output probability falls between:

```
0.40 and 0.60
```

If it does, the application returns:

> "Uncertain prediction. Try a clearer image."

Otherwise, it displays the predicted class along with its confidence score.

---

## Model Information

### Validation Model

- MobileNetV2
- Pre-trained on ImageNet
- Used only for detecting whether the uploaded image contains a banana

### Classification Model

- File: `banana_model.keras`
- Custom TensorFlow/Keras model
- Trained to classify bananas into:
  - Ripe
  - Unripe

---

## Supported Image Formats

- `.jpg`
- `.jpeg`
- `.png`

---

## Technologies Used

- Python
- Streamlit
- TensorFlow / Keras
- MobileNetV2
- NumPy
- Pillow (PIL)

---

## Notes

- Ensure that `banana_model.keras` is located in the same directory as `app.py`.
- Good lighting and clear images generally improve prediction accuracy.
- Images that are not recognized as bananas will be rejected before classification.

---

## Future Improvements

- Support additional ripeness stages (e.g., Green, Turning, Ripe, Overripe).
- Batch image prediction.
- Display Grad-CAM visualizations for model interpretability.
- Mobile-friendly interface.
- Model performance metrics and evaluation dashboard.

---
Reg Number:23/EG/EE/009
## License

This project is intended for educational and research purposes. Modify and use it according to your project's licensing requirements.
=======

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
=======
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
=======
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
=======



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
=======
Banana Ripeness Detection

Overview

Banana Ripeness Detection is a Streamlit-based web application that uses a TensorFlow deep learning model to classify whether a banana is Ripe or Unripe from an uploaded image. Before making a prediction, the application validates that the uploaded image is actually a banana using the pre-trained MobileNetV2 ImageNet model, helping to reduce incorrect predictions.

Features

- Upload banana images in JPG, JPEG, or PNG format.
- Validates that the uploaded image contains a banana before classification.
- Classifies bananas as Ripe or Unripe.
- Displays the prediction confidence score.
- Warns users when the model is uncertain and recommends uploading a clearer image.
- Simple and interactive web interface built with Streamlit.
- Efficient model loading through Streamlit resource caching.

Technologies Used

- Python
- Streamlit
- TensorFlow / Keras
- MobileNetV2 (ImageNet)
- NumPy
- Pillow (PIL)

Installation

1. Clone the repository.

git clone https://github.com/petersemmanuel13092006-code/EE20-Project.git

2. Navigate to the project directory.

cd EE20-Project

3. (Optional) Create and activate a virtual environment.

python -m venv venv

Windows

venv\Scripts\activate

Linux/macOS

source venv/bin/activate

4. Install the required dependencies.

pip install -r requirements.txt

How to Run

Start the application with:

streamlit run app.py

The application will open in your default web browser.

Usage

1. Launch the application.
2. Upload an image of a banana.
3. The application validates whether the uploaded image contains a banana.
4. If validation succeeds, the model predicts whether the banana is Ripe or Unripe.
5. The prediction and confidence score are displayed.
6. If the prediction confidence is low, the application recommends uploading a clearer image.

Screenshots

Home Page

«Screenshot goes here.»

Prediction Result

«Screenshot goes here.»

Future Improvements

- Support additional ripeness categories.
- Improve prediction accuracy using a larger dataset.
- Add graphical confidence visualization.
- Enable image capture directly from a device camera.
- Deploy the application online for public access.

Contributing

Contributions are welcome. To contribute:

1. Fork the repository.
2. Create a new branch.
3. Make your changes.
4. Commit your changes.
5. Push your changes.
6. Open a Pull Request.

License

This project is intended for educational purposes. An open-source license such as the MIT License may be added in the future.

Author

Peter Emmanuel

GitHub: https://github.com/petersemmanuel13092006-code

Acknowledgements

- TensorFlow and Keras
- Streamlit
- MobileNetV2 (ImageNet)
- The open-source Python community

Registration Number

Reg No: 23/EG/EE/029
