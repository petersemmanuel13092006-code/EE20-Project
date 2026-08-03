# EE20-Project
GET 324 mini project for group EE20

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
