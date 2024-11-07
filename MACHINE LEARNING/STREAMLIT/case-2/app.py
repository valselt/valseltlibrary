import streamlit as st
import torch
from torchvision import transforms
from PIL import Image
import timm
import json
import os
import requests

# URL untuk dataset labels
LABELS_URL = "https://raw.githubusercontent.com/anishathalye/imagenet-simple-labels/master/imagenet-simple-labels.json"
LABELS_PATH = "imagenet_labels.json"

# Fungsi untuk mengunduh dataset jika belum ada
def download_labels(url, path):
    if not os.path.exists(path):
        response = requests.get(url)
        if response.status_code == 200:
            with open(path, "wb") as file:
                file.write(response.content)
            print(f"Labels downloaded successfully and saved as '{path}'")
        else:
            print(f"Failed to download labels. Status code: {response.status_code}")

# Panggil fungsi untuk mengunduh labels jika belum ada
download_labels(LABELS_URL, LABELS_PATH)

# Load model and labels
@st.cache_resource
def load_model():
    model = timm.create_model('efficientnet_b0', pretrained=True)
    model.eval()
    return model

@st.cache_data
def load_labels():
    with open(LABELS_PATH, 'r') as f:
        labels = json.load(f)
    return labels

def process_image(image):
    # Define image transforms
    transform = transforms.Compose([
        transforms.Resize(256),
        transforms.CenterCrop(224),
        transforms.ToTensor(),
        transforms.Normalize([0.485, 0.456, 0.406], 
                             [0.229, 0.224, 0.225])
    ])
    return transform(image).unsqueeze(0)

def main():
    st.title("🍔 Food Image Classifier")
    st.write("Upload gambar makanan untuk klasifikasi")
    
    # Load model and labels
    model = load_model()
    labels = load_labels()
    
    # File uploader
    uploaded_file = st.file_uploader("Pilih gambar makanan...", type=["jpg", "jpeg", "png"])
    
    if uploaded_file:
        # Display image
        image = Image.open(uploaded_file).convert('RGB')
        st.image(image, caption='Uploaded Image', use_column_width=True)
        
        # Add prediction button
        if st.button("Classify"):
            with st.spinner("Classifying..."):
                # Process image
                input_tensor = process_image(image)
                
                # Get prediction
                with torch.no_grad():
                    output = model(input_tensor)
                    probabilities = torch.nn.functional.softmax(output[0], dim=0)
                
                # Get top 5 predictions
                top5_prob, top5_idx = torch.topk(probabilities, 5)
                
                # Display results
                st.subheader("Classification Results:")
                for i in range(5):
                    prob = top5_prob[i].item()
                    label = labels[top5_idx[i].item()]  # Gunakan indeks dari dataset JSON
                    
                    # Create a progress bar for each prediction
                    st.write(f"**{label}**")
                    st.progress(prob)
                    st.write(f"Confidence: {prob:.2%}")
                    st.write("---")

if __name__ == "__main__":
    main()
