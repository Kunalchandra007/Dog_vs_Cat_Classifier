# Dog vs Cat Image Classifier 🐶🐱

This project is a deep learning-based image classifier that can distinguish between dogs and cats using a Convolutional Neural Network (CNN). The model is trained using TensorFlow and Keras, and it is deployed with a user-friendly interface using Streamlit.

## 📌 Features
- Classifies images as either a **Dog** or a **Cat**
- Built with a **Convolutional Neural Network (CNN)**
- Utilizes **TensorFlow** and **Keras** for model training
- Includes **image preprocessing** and **normalization**
- Interactive UI via **Streamlit** for image upload and prediction

## 🧠 Model Architecture
- 4 Convolutional Layers with ReLU activation and MaxPooling
- Fully connected Dense layers
- Sigmoid activation for binary classification

## 🧪 Dataset
- Used the **Dogs vs Cats** dataset from Kaggle
- Dataset is split into training and validation sets
- Images are resized to 256x256 and normalized between 0 and 1

## 🚀 Deployment
- Deployed using **Streamlit** for web-based inference
- Hosted using **ngrok** to generate a public URL (optional for Colab users)

## 📂 Files
- `dog_vs_cat_classification.py`: Main training and evaluation script
- `dog_cat_model.h5`: Saved trained model
- `app.py`: Streamlit application for prediction

## 🖼️ Example
Upload an image using the Streamlit app, and it will predict whether it’s a dog or a cat!

## 🔧 How to Run (Locally or Google Colab)
1. Clone the repository
2. Ensure all dependencies are installed:
   ```bash
   pip install tensorflow keras streamlit pyngrok opencv-python
   ```
3. Run the app locally:
   ```bash
   streamlit run app.py
   ```
4. If using Google Colab and ngrok:
   - Install and configure `pyngrok` with your authtoken
   - Use the following in your notebook:
     ```python
     from pyngrok import ngrok
     public_url = ngrok.connect(port=8501)
     print("Streamlit App Link:", public_url)
     ```

## 👤 Author
Made with ❤️ by **Kunal Chandra**
