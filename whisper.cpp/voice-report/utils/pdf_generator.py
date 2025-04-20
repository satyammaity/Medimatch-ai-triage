from fpdf import FPDF
from datetime import datetime
import os

def generate_pdf(transcription, output_path):
    # Ensure the output folder exists
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    pdf.cell(200, 10, txt="MediMatch Medical Report", ln=True, align='C')
    pdf.ln(10)

    pdf.cell(200, 10, txt=f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}", ln=True)
    pdf.ln(10)

    pdf.set_font("Arial", size=11)
    pdf.multi_cell(0, 10, txt=transcription)

    pdf.output(output_path)