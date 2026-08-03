# EE20-Project
GET 324 mini project for group EE20
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
