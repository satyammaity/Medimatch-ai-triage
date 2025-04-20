# MediMatch – AI-Powered Emergency Triage Assistant

MediMatch is an AI-powered medical triage assistant that helps users communicate symptoms through voice or text input. It transcribes audio using OpenAI’s Whisper, classifies the severity using a custom NLP model, and generates a downloadable medical report PDF with AI reasoning.

## 🔍 Project Overview

This project provides a fast and accessible way for individuals to report medical emergencies, especially in situations where typing is difficult. Users can either speak or type their symptoms, and the system will generate a severity classification and reasoning, presented in a downloadable PDF report.

## ✨ Features

- 🎤 Voice-to-text transcription via OpenAI Whisper
- 🧠 NLP-based severity classification of symptoms
- 📄 PDF generation of the final report
- 🌐 Responsive Angular frontend with dark/light mode
- ⚡ Flask backend API with seamless proxy integration

## 🛠 Technologies Used

- Frontend: Angular, Bootstrap 5
- Backend: Python, Flask
- AI Model: Whisper (base model), custom NLP classifier
- PDF Generation: FPDF
- APIs: None (all models are locally run)
- Version Control: Git & GitHub

## 📁 Folder Structure

```
medimatch/
├── client/               # Angular frontend
│   └── src/app/...       # Components, assets, styles
├── server/               # Flask backend (transcription, classification, PDF)
│   ├── app.py            # Main backend server
│   ├── severity_classifier.py
│   └── pdf_generator.py
├── whisper.cpp/          # Optional or experimental whisper integration
├── proxy.conf.json       # Proxy setup for Angular → Flask
├── requirements.txt      # Python dependencies
└── README.md
```

## ⚙️ Setup and Installation

### Prerequisites

- Node.js + Angular CLI (for frontend)
- Python 3.9+ and pip (for backend)
- Git

### Clone the Repository

```bash
git clone https://github.com/your-username/medimatch.git
cd medimatch
```

### Setup Backend (Flask)

```bash
cd server
pip install -r requirements.txt
python app.py
```

Make sure Whisper model downloads successfully during first run.

### Setup Frontend (Angular)

```bash
cd client
npm install
ng serve --proxy-config proxy.conf.json
```

### Proxy Configuration

The Angular frontend uses proxy.conf.json to forward API calls to Flask:

```json
{
  "/api": {
    "target": "http://localhost:5000",
    "secure": false,
    "changeOrigin": true
  }
}
```

## 🧪 Usage Instructions

- Open the Angular frontend in your browser.
- Enter your name and either record audio or type your symptoms.
- Click “Generate Report”.
- Wait for processing, then download the PDF.

## 🎥 Demo Video
[A short demo video showcasing all
](https://drive.google.com/file/d/1QHfp4NXFyklHjhPA7XUvfMw3A-FoVTWz/view?usp=drive_link)

## 👥 Team Members
- https://github.com/satyammaity (Cyber Forensics & InfoSec – Technique Polytechnic Institute)
- https://github.com/Darklord900 (Cyber Forensics & InfoSec – Technique Polytechnic Institute)
- https://github.com/Sounil05 (Cyber Forensics & InfoSec – Technique Polytechnic Institute)
-  https://github.com/akash007-0 (Cyber Forensics & InfoSec – Technique Polytechnic Institute)

## 📄 License

This project is open-source under the MIT License.
