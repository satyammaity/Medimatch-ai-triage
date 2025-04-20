# file: generate_report.py

import os
import whisper
from fpdf import FPDF
from datetime import datetime

# Load whisper model
model = whisper.load_model("base")

# Input audio file
audio_path = input("Enter audio file name (e.g. test1.mp3): ").strip()
if not os.path.exists(audio_path):
    print("Audio file not found!")
    exit(1)

# Transcribe
print("Transcribing audio...")
result = model.transcribe(audio_path)
transcription = result["text"]

# Get user input
patient_name = input("Enter Patient Name: ").strip()
date_today = input("Enter Date (YYYY-MM-DD) or press enter for today: ").strip()
if not date_today:
    date_today = datetime.today().strftime('%Y-%m-%d')

# Prepare PDF
pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size=12)

pdf.cell(200, 10, txt="Medical Audio Report", ln=True, align='C')
pdf.ln(10)
pdf.cell(200, 10, txt=f"Patient Name: {patient_name}", ln=True)
pdf.cell(200, 10, txt=f"Date: {date_today}", ln=True)
pdf.cell(200, 10, txt=f"Audio File: {audio_path}", ln=True)
pdf.ln(10)
pdf.multi_cell(0, 10, txt=transcription)

# Save
if not os.path.exists("reports"):
    os.makedirs("reports")

filename = f"reports/{patient_name.replace(' ', '')}{date_today}.pdf"
pdf.output(filename)

print(f"PDF generated: {filename}")