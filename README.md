# MediMatch: AI-Powered Emergency Triage System

## 🧠 Overview
MediMatch is an intelligent web application that uses AI to transcribe audio/text-based medical symptoms, classify their severity using NLP techniques, and generate a downloadable emergency report in PDF format.

## 🚀 Features
- 🎤 Voice and 📝 text-based symptom input
- 🧠 Whisper AI for real-time audio transcription
- 🚨 Severity classification using NLP
- 📄 Downloadable PDF emergency report
- 🌗 Light/Dark mode toggle UI
- ⚙️ Simple to deploy with Flask & Angular

## 👨‍💻 Technologies Used
- Angular 17 (Frontend)
- Flask (Backend API)
- OpenAI Whisper (Speech-to-Text)
- Python (NLP, PDF generation)
- Bootstrap 5, Icons, FPDF

## 📦 Setup & Installation

### 📁 Backend (Flask)
```bash
cd backend
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
python app.py
```

### 🌐 Frontend (Angular)
```bash
cd frontend
npm install
ng serve --proxy-config proxy.conf.json
```

## 📂 Folder Structure
```
root
├── backend
│   ├── app.py
│   ├── severity_classifier.py
│   ├── pdf_generator.py
│   ├── uploads/
│   └── output/
├── frontend
│   └── src/app/components/upload
│       ├── upload.component.ts / html / css
│       └── services
├── proxy.conf.json
└── README.md
```

## 🔗 Live Demo
[Insert demo video link here — YouTube/Drive]

## 👥 Team Members
- Your Name
- Teammate Name 2
- Teammate Name 3

## 📌 Notes
- All audio uploads are stored temporarily and deleted after report generation.
- The `proxy.conf.json` is used to redirect API requests from Angular to Flask to avoid CORS.

## 📃 License
This project is licensed for educational and hackathon use only.

---

> Be prepared to present and defend your project during evaluations.
> Only public repositories submitted via HackQuest will be considered.
