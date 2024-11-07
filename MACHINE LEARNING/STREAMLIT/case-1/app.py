# emotion_app.py
import streamlit as st
from transformers import pipeline
import plotly.graph_objects as go
from datasets import load_dataset

dataset = load_dataset("emotion")

# Load model
@st.cache_resource
def load_model():
    return pipeline("text-classification", 
                   model="bhadresh-savani/distilbert-base-uncased-emotion",
                   top_k=None)

def create_emotion_chart(emotions):
    # Create pie chart
    fig = go.Figure(data=[go.Pie(
        labels=[e['label'] for e in emotions],
        values=[e['score'] for e in emotions],
        hole=.3
    )])
    return fig

def main():
    st.title("💭 Emotion Detection App")
    st.write("Deteksi emosi dari teks menggunakan DistilBERT")
    
    # Load model
    classifier = load_model()
    
    # Text input
    text = st.text_area("Masukkan teks yang ingin dianalisis:", 
                        "I am really happy today!")
    
    if st.button("Analyze"):
        with st.spinner("Analyzing..."):
            # Get prediction
            emotions = classifier(text)[0]
            
            # Display results
            col1, col2 = st.columns([2,3])
            
            with col1:
                st.subheader("Emotions Detected:")
                for emotion in emotions:
                    st.write(f"**{emotion['label']}**: {emotion['score']:.2%}")
            
            with col2:
                st.subheader("Visualization")
                fig = create_emotion_chart(emotions)
                st.plotly_chart(fig)
            
            # Show text analysis
            st.subheader("Text Analysis")
            dominant_emotion = max(emotions, key=lambda x: x['score'])
            st.write(f"Dominant emotion: **{dominant_emotion['label']}** "
                    f"with {dominant_emotion['score']:.2%} confidence")

if __name__ == "__main__":
    main()