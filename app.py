import gradio as gr
import tensorflow as tf
import numpy as np
from PIL import Image

# Load model
model = tf.keras.models.load_model("space_classifier_model.keras")

class_names = ['galaxy', 'star']

def predict(image):
    image = image.resize((128,128))
    img_array = np.array(image) / 255.0
    img_array = np.expand_dims(img_array, axis=0)

    prediction = model.predict(img_array)
    predicted_class = class_names[np.argmax(prediction)]
    confidence = np.max(prediction) * 100

    return f"{predicted_class} ({confidence:.2f}%)"

interface = gr.Interface(
    fn=predict,
    inputs=gr.Image(type="pil"),
    outputs="text",
    title="🚀 Space Image Classifier",
    description="Upload an astronomical image to classify it as Star or Galaxy"
)

interface.launch()