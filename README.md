
---

# Handwritten Digit Recognition — `README.md`

```md id="k8w2yn"
# Handwritten Digit Recognition using Deep Learning

## Project Overview

This project is a Deep Learning based handwritten digit recognition system built using TensorFlow and Keras.

The model is trained on the MNIST dataset and can predict handwritten digits from uploaded images through a Streamlit web application.

---

## Features

- Handwritten digit prediction
- Image upload functionality
- Deep Learning based prediction
- Streamlit web application
- Real-time digit recognition

---

## Technologies Used

- Python
- TensorFlow
- Keras
- Streamlit
- NumPy
- Pillow
- Matplotlib

---

## Dataset Information

The model is trained using the MNIST dataset containing:

- 60,000 training images
- 10,000 testing images

Each image:
- Size: 28 × 28
- Grayscale handwritten digits
- Digits from 0 to 9

---

## Model Architecture

Input Layer:
- Flatten layer (28 × 28 → 784)

Hidden Layer:
- Dense layer with 100 neurons (ReLU)

Output Layer:
- Dense layer with 10 neurons (Sigmoid)

Optimizer:
- Adam

Loss Function:
- Sparse Categorical Crossentropy

---

## Project Structure

```text
handwritten_digit_project/
│
├── train_model.ipynb
├── mnist_model.keras
├── app.py
├── requirements.txt
└── README.md
