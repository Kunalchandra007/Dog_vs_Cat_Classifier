import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image

# Load model
model = tf.keras.models.load_model("dog_cat_model.h5")

st.title("🐶🐱 Dog vs Cat Classifier")
st.write("Upload an image to classify it as a Dog or a Cat.")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file).convert('RGB')
    st.image(image, caption='Uploaded Image', use_column_width=True)

    # Preprocess
    image = image.resize((256, 256))
    img_array = np.array(image) / 255.0
    img_array = img_array.reshape((1, 256, 256, 3))

    prediction = model.predict(img_array)
    class_name = "Dog 🐶" if prediction[0][0] > 0.5 else "Cat 🐱"
    
    st.success(f"Prediction: **{class_name}**")
