import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image, ImageOps

# Load trained model
model = tf.keras.models.load_model("mnist_model.keras")

st.title("Handwritten Digit Recognition")

uploaded_file = st.file_uploader(
    "Upload Digit Image",
    type=["png", "jpg", "jpeg"]
)

if uploaded_file is not None:

    image = Image.open(uploaded_file).convert("L")

    image = ImageOps.invert(image)

    image = image.resize((28, 28))

    st.image(image, caption="Uploaded Image", width=150)

    img_array = np.array(image)

    img_array = 255 - img_array

    img_array = img_array / 255.0

    img_array = img_array.reshape(1, 28, 28)

    prediction = model.predict(img_array)

    predicted_digit = np.argmax(prediction)

    st.success(f"Predicted Digit : {predicted_digit}")