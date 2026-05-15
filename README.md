

# Handwritten Digit Recognition using Deep Learning

## Overview

This project is a Deep Learning based Handwritten Digit Recognition System developed using TensorFlow and Keras. The application is trained on the MNIST dataset and deployed using Streamlit.

The system can recognize handwritten digits from uploaded images and predict the digit in real time.

---

## Project Objective

The main objective of this project is to understand and implement a Deep Learning workflow for image classification using Artificial Neural Networks (ANN).

The model learns pixel patterns from handwritten digit images and predicts digits from 0 to 9.

---

## Features

- Handwritten digit recognition
- Real-time image prediction
- Image upload support
- Deep Learning based classification
- Streamlit web application
- MNIST dataset implementation
- Image preprocessing and normalization

---

## Technologies Used

| Technology | Purpose |
|---|---|
| Python | Programming Language |
| TensorFlow | Deep Learning Framework |
| Keras | Neural Network API |
| Streamlit | Web Application Framework |
| NumPy | Numerical Operations |
| Pillow | Image Processing |
| Matplotlib | Data Visualization |

---

## Dataset Information

The model is trained using the MNIST handwritten digit dataset.

### Dataset Details

- 60,000 training images
- 10,000 testing images
- 28 × 28 grayscale images
- Digits from 0 to 9

Each image contains handwritten numerical digits represented as pixel intensity values.

---

## Deep Learning Workflow

### 1. Data Loading
The MNIST dataset is loaded directly from Keras datasets.

### 2. Data Preprocessing
- Pixel normalization
- Image reshaping
- Flattening image data

### 3. Model Building
An Artificial Neural Network is created using Dense layers.

### 4. Model Training
The model learns handwritten digit patterns using training images.

### 5. Prediction
The trained model predicts uploaded handwritten digit images.

---

## Model Architecture

### Input Layer
- 28 × 28 image pixels

### Hidden Layer
- Dense Layer with 100 neurons
- ReLU activation function

### Output Layer
- Dense Layer with 10 neurons
- Sigmoid activation function

### Optimizer
- Adam Optimizer

### Loss Function
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
