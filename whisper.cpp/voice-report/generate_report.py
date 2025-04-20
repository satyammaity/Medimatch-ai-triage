from fpdf import FPDF
import os


def generate_pdf(transcription, output_path='report.pdf'):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    pdf.set_text_color(40, 40, 40)
    pdf.cell(200, 10, txt="MediMatch Voice Transcription Report", ln=True, align='C')
    pdf.ln(10)

    for line in transcription.split('\n'):
        pdf.multi_cell(0, 10, txt=line)

    pdf.output(output_path)
    print(f"PDF saved as {output_path}")


if __name__ == "__main__":
    print("=== MediMatch Voice to PDF Generator ===")
    audio_path = input("Enter audio file path (e.g., audio/test1.mp3): ")

    import whisper

    try:
        print("Transcribing audio...")
        model = whisper.load_model("base")
        result = model.transcribe(audio_path)
        generate_pdf(result["text"])
    except Exception as e:
        print("Something went wrong:", e)