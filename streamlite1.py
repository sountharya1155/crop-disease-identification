

import streamlit as st
import requests
from PIL import Image
import base64
import pandas as pd
import io

# Page Configuration
st.set_page_config(page_title="CropCure – AI Helper for Farmers", page_icon="🌾", layout="centered")

# ---------- Custom CSS for Background & Styling ----------
st.markdown("""
    <style>
        body {
            background-color: #f5f5f5;
        }
        .reportview-container {
            background: #f0f8ff;
        }
        .block-container {
            padding-top: 2rem;
        }
        .stButton>button {
            background-color: #4CAF50;
            color: white;
            font-weight: bold;
            border-radius: 8px;
        }
    </style>
""", unsafe_allow_html=True)

# ---------- Optional: Add a Banner Image ----------
def set_background_from_local(image_path):
    with open(image_path, "rb") as img_file:
        encoded = base64.b64encode(img_file.read()).decode()
    st.markdown(
        f"""
        <div style="text-align:center;">
            <img src="data:image/png;base64,{encoded}" width="80%" style="border-radius: 15px; margin-bottom: 20px;" />
        </div>
        """, unsafe_allow_html=True
    )

set_background_from_local("D:\\AI HELPER FOR FARMERS PROJECT\\utils\\banner.jpg")


# ---------- App Title ----------
st.title("🌾 CropCure – AI Helper for Farmers")

st.markdown("### 👇 Select the type of input:")
option = st.radio("Select input type", ["📷 Image", "🎤 Voice"], label_visibility="collapsed")

# ---------- Image Section ----------
if option == "📷 Image":
    st.markdown("#### 🖼️ Upload a crop leaf image for disease prediction:")
    uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])
    
    if uploaded_file:
        with st.spinner("🔍 Analyzing image..."):
            response = requests.post(
                "http://localhost:8000/classify-image/",
                files={"file": uploaded_file}
            )
        prediction = response.json().get("prediction", "Error")
        st.success(f"🩺 Predicted Disease: **{prediction}**")

        with st.spinner("💡 Fetching treatment recommendation..."):
            diagnose = requests.post(
                "http://localhost:8000/diagnose/",
                json={
                    "question": "How to treat it?",
                    "disease_name": prediction
                }
            )
        answer = diagnose.json().get("answer", "No answer found.")
        st.info(f"💡 **Suggested Solution**: {answer}")

        # Excel Export
        df = pd.DataFrame({
            "Prediction": [prediction],
            "Recommendation": [answer]
        })
        buffer = io.BytesIO()
        with pd.ExcelWriter(buffer, engine='xlsxwriter') as writer:
            df.to_excel(writer, index=False, sheet_name="Result")
        excel_data = buffer.getvalue()

        st.download_button(
            label="📥 Download Result as Excel",
            data=excel_data,
            file_name="crop_diagnosis_result.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )

# ---------- Voice Section ----------
elif option == "🎤 Voice":
    st.markdown("#### 🎤 Upload your voice query:")
    uploaded_audio = st.file_uploader("Upload a voice file", type=["mp3", "wav"])

    if uploaded_audio:
        with st.spinner("📝 Transcribing your voice..."):
            response = requests.post(
                "http://localhost:8000/transcribe-audio/",
                files={"file": uploaded_audio}
            )
        transcription = response.json().get("transcription", "Error")
        st.text_area("📝 Transcribed Text", transcription, height=100)

        disease_name = st.text_input("🔍 Enter the suspected disease name (e.g., Potato___Early_blight)")

        if st.button("💡 Get Solution") and disease_name:
            with st.spinner("🔎 Searching for a solution..."):
                diagnose = requests.post(
                    "http://localhost:8000/diagnose/",
                    json={
                        "question": transcription,
                        "disease_name": disease_name
                    }
                )
            answer = diagnose.json().get("answer", "No answer found.")
            st.success("💡 **Suggested Solution**: " + answer)

            # Excel Export for voice section
            df = pd.DataFrame({
                "Transcribed Question": [transcription],
                "Disease Name": [disease_name],
                "Recommendation": [answer]
            })
            buffer = io.BytesIO()
            with pd.ExcelWriter(buffer, engine='xlsxwriter') as writer:
                df.to_excel(writer, index=False, sheet_name="Voice_Result")
            excel_data = buffer.getvalue()

            st.download_button(
                label="📥 Download Result as Excel",
                data=excel_data,
                file_name="voice_diagnosis_result.xlsx",
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            )

# ---------- Summary Section ----------
st.markdown("---")
st.markdown("###  Summary Report")
st.markdown("""
This tool helps farmers:

- Detect plant diseases using AI  
- Get practical treatment tips instantly  
- Use either image or voice as input  
- Reduce pesticide misuse and improve crop yield  
""")

st.markdown("---")
st.caption(" Developed with  to support smart, sustainable agriculture.")



