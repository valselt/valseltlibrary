# app_keras.py
import streamlit as st
import numpy as np
from tensorflow.keras.models import load_model

# Fungsi untuk memuat dan menggunakan model Keras
def load_keras_model():
    model = load_model("keras_model.h5")  # Path ke file model h5
    return model

# Fungsi prediksi untuk model Keras
def predict_keras(model, input_data):
    prediction = model.predict(input_data)
    return prediction

st.title("Prediksi dengan Model Keras (.h5)")

# Input data untuk prediksi
input_data = st.text_input("Masukkan 4 nilai untuk prediksi, dipisahkan dengan koma:")

if input_data:
    input_data = np.array([float(x) for x in input_data.split(",")]).reshape(1, -1)

    # Load dan prediksi dengan model
    model = load_keras_model()
    prediction = predict_keras(model, input_data)

    st.write("Hasil Prediksi:", prediction)
