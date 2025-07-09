#  CropCure – AI Helper for Farmers

**CropCure** is an AI-powered web application that assists farmers in diagnosing crop diseases and receiving treatment recommendations. The system accepts **image inputs of crop leaves** and **voice queries** for convenience, especially in rural agricultural scenarios.

---

##  Features

-  **Image-Based Disease Detection**  
  Upload a leaf image to get a disease prediction from the backend model.

-  **Voice-Based Query Support**  
  Upload your voice query in `.mp3` or `.wav` format, and the app will transcribe it into text using the backend.

-  **Treatment Recommendation**  
  Based on the diagnosed disease, the system provides an AI-generated treatment recommendation.

-  **Download Results as Excel**  
  Users can download the prediction and suggested treatment as an `.xlsx` report for future reference.

---

## 🛠️ Tech Stack

| Layer     | Technology         |
|-----------|--------------------|
| Frontend  | [Streamlit](https://streamlit.io) |
| Backend   | [FastAPI](https://fastapi.tiangolo.com) |
| Image     | [Pillow](https://python-pillow.org/) |
| Audio     | Handled as binary files, transcribed via backend |

---

## 📁 Project Structure

```
AI_Helper/
│
├── __pycache__/               # Python cache files
├── data/                      # Directory for datasets
├── models/                    # Contains trained models
│   └── resnet18_crop_model/   # Specific ResNet18 model variant
│
├── notebooks/                 # Jupyter notebooks for experimentation
│   ├── evaluate_model.ipynb   # Notebook for evaluating models
│   └── train_model.ipynb      # Notebook for training models
│
├── refer/                     # (Optional: describe this folder if used)
├── temp/                      # Temporary files and scripts
│
├── utils/                     # Utility functions and assets
│   ├── __init__.py            
│   ├── banner.jpg             # Banner image for UI or reports
│   └── solutions.py           # Reusable utility functions
│
├── venv/                      # Python virtual environment
│
├── app.py                     # Main application script
├── crop_model.py              # Image cropping/model script
├── diagnose_issue.py          # Diagnostic tools or error handling
├── requirements.txt           # List of Python dependencies
├── streamlite1.py             # Streamlit app file
└── voice_to_text.py           # Voice recognition module
```


## Setup Instructions
Backend (FastAPI)

cd backend/
python -m venv venv
venv\Scripts\activate             # On Windows
pip install -r requirements.txt

uvicorn main:app --reload         # Runs at http://localhost:8000

##  Excel Report Download
After a successful diagnosis (from image or voice input), users can download a well-formatted Excel report containing:
-- The diagnosed disease
-- The suggested treatment
This allows for easy sharing, record-keeping, or printing.

##  Purpose
**CropCure is built to support:**
-- Smallholder and marginal farmers
-- Agricultural officers and field workers
-- Real-time, low-barrier crop disease diagnosis

-- It helps reduce guesswork and pesticide misuse
--  It improves crop yield and sustainability
--  It is designed to be accessible and easy to use

## License
This project is open-source. 




