import os
import streamlit as st
import numpy as np
from PIL import Image
import tensorflow as tf

imgsize = 224
classnames = ["Ripe", "Unripe"]

st.set_page_config(page_title="Banana Ripeness Detection", page_icon="🍌")

st.title("Banana Ripeness Detection")
st.write("Upload a photo of a banana to check if it's ripe or unripe.")


@st.cache_resource
def loadvalidationnetwork():
    return tf.keras.applications.mobilenet_v2.MobileNetV2(weights="imagenet")


@st.cache_resource
def loadbananamodel():
    currentfolder = os.path.dirname(__file__)
    modelpath = os.path.join(currentfolder, "banana_model.keras")
    return tf.keras.models.load_model(modelpath)


validationnetwork = loadvalidationnetwork()
bananamodel = loadbananamodel()

uploadedfile = st.file_uploader("Choose an image", type=["jpg", "jpeg", "png"])

if uploadedfile is not None:
    image = Image.open(uploadedfile).convert("RGB")
    st.image(image, caption="Uploaded image", use_container_width=True)

    preprocessinput = tf.keras.applications.mobilenet_v2.preprocess_input
    decodepredictions = tf.keras.applications.mobilenet_v2.decode_predictions

    resizedforvalidation = image.resize((224, 224))
    validationarray = np.array(resizedforvalidation)
    expandedarray = np.expand_dims(validationarray, axis=0)
    preppedarray = preprocessinput(expandedarray.copy())
    validationresult = validationnetwork.predict(preppedarray, verbose=0)
    decodedpredictions = decodepredictions(validationresult, top=10)[0]

    validtags = ["banana", "fruit", "plantain"]
    isvalidbanana = any(
        any(tag in label.lower() for tag in validtags) and confidence > 0.01
        for (code, label, confidence) in decodedpredictions
    )

    if not isvalidbanana:
        st.error("This doesn't look like a banana. Please upload a clearer photo of a banana.")
    else:
        resized = image.resize((imgsize, imgsize))
        arr = np.array(resized, dtype="float32") / 255.0
        arr = np.expand_dims(arr, axis=0)

        prediction = bananamodel.predict(arr, verbose=0)[0][0]

        if 0.4 <= prediction <= 0.6:
            st.warning(f"Uncertain prediction (confidence: {prediction:.2f}). Try a clearer image.")
        else:
            label = classnames[1] if prediction > 0.5 else classnames[0]
            confidence = prediction if prediction > 0.5 else 1 - prediction
            st.success(f"Prediction: **{label}** (confidence: {confidence:.2%})")