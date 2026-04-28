import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image

# Load model
model = tf.keras.models.load_model("space_classifier_model.keras")

# Class names
class_names = ['galaxy', 'star']

# UI Title
st.title("🚀 AI-Powered Space Object Classifier")
st.write("Classifies astronomical images into Stars or Galaxies using Deep Learning.")

# File uploader
uploaded_file = st.file_uploader("Upload an image", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    # Load and display image
    image = Image.open(uploaded_file).resize((128, 128))
    st.image(image, caption="Uploaded Image")

    # Preprocess image
    img_array = np.array(image) / 255.0
    img_array = np.expand_dims(img_array, axis=0)

    try:
        # Prediction
        prediction = model.predict(img_array)
        predicted_class = class_names[np.argmax(prediction)]
        confidence = np.max(prediction) * 100

        # Display results
        st.subheader("Prediction Result")
        st.write(f"Prediction: {predicted_class} ({confidence:.2f}%)")

        st.write("Galaxy probability:", float(prediction[0][0]))
        st.write("Star probability:", float(prediction[0][1]))

    except Exception as e:
        st.error("Error processing image. Try another image.")