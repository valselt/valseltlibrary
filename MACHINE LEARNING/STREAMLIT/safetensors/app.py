import streamlit as st
import torch
from torch import nn
from torch.utils.data import DataLoader, TensorDataset
from safetensors.torch import save_file, load_file
import numpy as np
from sklearn.preprocessing import MinMaxScaler

# Model Arsitektur
class GraduationPredictor(nn.Module):
    def __init__(self):
        super(GraduationPredictor, self).__init__()
        self.fc1 = nn.Linear(4, 16)
        self.fc2 = nn.Linear(16, 8)
        self.fc3 = nn.Linear(8, 2)

    def forward(self, x):
        x = torch.relu(self.fc1(x))
        x = torch.relu(self.fc2(x))
        return torch.softmax(self.fc3(x), dim=1)

# Fungsi untuk memuat model
def load_model(model_path):
    model = GraduationPredictor()
    loaded_state_dict = load_file(model_path)
    model.load_state_dict(loaded_state_dict)
    model.eval()  # Set model ke mode evaluasi
    return model

# Simulasi dataset untuk prediksi (normalisasi dan pelatihan tidak diperlukan lagi di sini)
def get_scaler():
    X = np.array([
        [5, 2, 80, 75],
        [3, 1, 60, 55],
        [10, 3, 90, 85],
        [7, 2, 85, 70],
        [4, 1, 50, 45],
        [12, 3, 95, 90],
        [6, 2, 70, 60],
        [15, 3, 85, 88],
        [2, 1, 40, 35],
        [8, 3, 80, 78],
        [9, 2, 65, 68],
        [1, 1, 30, 25],
        [11, 3, 95, 90],
        [5, 2, 70, 65],
        [13, 3, 88, 85],
        [7, 1, 55, 58],
        [14, 2, 92, 95],
        [3, 1, 45, 42],
        [10, 3, 85, 82],
        [12, 2, 78, 75],
        [6, 2, 60, 55],
        [9, 2, 80, 77],
        [7, 2, 72, 70],
        [4, 1, 50, 48],
        [11, 3, 94, 92],
        [5, 2, 65, 63],
        [8, 2, 75, 72],
        [2, 1, 40, 37],
        [13, 3, 90, 88],
        [6, 1, 55, 53],
        [14, 3, 96, 93]
    ], dtype=np.float32)

    scaler = MinMaxScaler()
    X_scaled = scaler.fit_transform(X)
    return scaler

# Path ke model yang sudah disimpan
model_path = "graduation_predictor_model.safetensors"

# Streamlit UI
st.title("Graduation Prediction System")
st.write("Masukkan data untuk memprediksi apakah seseorang akan lulus atau tidak.")

# Form input untuk fitur
study_time = st.slider("Waktu Belajar (jam)", 0, 20, 5)
exam_count = st.slider("Jumlah Ujian", 1, 5, 3)
attendance = st.slider("Kehadiran (%)", 0, 100, 80)
task_score = st.slider("Skor Tugas", 0, 100, 70)

# Proses input dan prediksi
if st.button("Prediksi"):
    # Menyiapkan input data untuk model
    input_data = np.array([[study_time, exam_count, attendance, task_score]], dtype=np.float32)
    
    # Load model
    model = load_model(model_path)
    scaler = get_scaler()
    input_scaled = scaler.transform(input_data)  # Normalisasi input berdasarkan scaler

    # Prediksi
    input_tensor = torch.tensor(input_scaled, dtype=torch.float32)
    with torch.no_grad():
        output = model(input_tensor)
        _, predicted = torch.max(output, 1)
    
    # Tampilkan hasil
    result = "Lulus" if predicted.item() == 1 else "Tidak Lulus"
    st.write(f"Prediksi: {result}")
