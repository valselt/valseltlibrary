import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Judul Aplikasi
st.title("Perkenalan Berbagai Komponen yang bisa dipakai di Streamlit")

# 1. Teks dan Header
st.header("1. Teks dan Header")
st.write("Komponen untuk menampilkan teks sederhana:")
st.text("Ini adalah teks biasa.")
st.markdown("Ini adalah **Markdown**. Bisa menampilkan teks dengan *format* ```khusus```.")
st.latex(r"e^{i\pi} + 1 = 0")  # Menampilkan rumus matematika

# 2. Komponen Input Dasar
st.header("2. Komponen Input Dasar")
name = st.text_input("Masukkan Nama Anda:")
age = st.number_input("Masukkan Umur Anda:", min_value=0, max_value=100, step=1)
st.write(f"Nama Anda: {name}, Umur: {age}")

# 3. Slider dan Selectbox
st.header("3. Slider dan Selectbox")
rating = st.slider("Berikan nilai (1-100):", 1, 100)
option = st.selectbox("Pilih Warna Favorit:", ["Merah", "Hijau", "Biru"])
st.write(f"Rating Anda: {rating}, Warna Favorit: {option}")

# 4. Checkbox, Radio, dan Button
st.header("4. Checkbox, Radio, dan Button")
agree = st.checkbox("Saya setuju dengan syarat dan ketentuan")
level = st.radio("Pilih Level:", ["Pemula", "Menengah", "Lanjutan"])
if st.button("Kirim"):
    st.write("Terima kasih telah mengirim data!")

# 5. Komponen Sidebar
st.sidebar.header("Sidebar")
theme_color = st.sidebar.color_picker("Pilih Warna Tema", "#00f900")
show_sidebar_info = st.sidebar.checkbox("Tampilkan Info di Sidebar")
if show_sidebar_info:
    st.sidebar.write("Ini adalah informasi tambahan di sidebar.")

# 6. Tabel dan DataFrame
st.header("6. Tabel dan DataFrame")
data = pd.DataFrame({
    "Kolom A": np.random.rand(5),
    "Kolom B": np.random.rand(5),
    "Kolom C": np.random.rand(5),
})
st.write("Data Frame:")
st.dataframe(data)

# 7. Grafik Sederhana
st.header("7. Grafik Sederhana")
x = np.linspace(0, 15, 100)
y = np.tan(x)
fig, ax = plt.subplots()
ax.plot(x, y)
st.pyplot(fig)

# 8. File Upload
st.header("8. File Upload")
uploaded_file = st.file_uploader("Pilih file untuk diupload")
if uploaded_file:
    st.write("Nama file:", uploaded_file.name)
    st.write("Tipe file:", uploaded_file.type)

# 9. Peta Geografis
st.header("9. Peta Geografis")
map_data = pd.DataFrame(
    np.random.randn(100, 2) / [50, 50] + [37.76, -122.4],
    columns=["lat", "lon"]
)
st.map(map_data)

# 10. Progress Bar
st.header("10. Progress Bar")
import time
progress_bar = st.progress(0)
for percent_complete in range(100):
    time.sleep(0.01)
    progress_bar.progress(percent_complete + 1)

st.write("Progress Bar selesai!")

