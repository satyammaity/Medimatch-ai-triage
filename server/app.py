from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from werkzeug.utils import secure_filename
import os
import whisper
from severity_classifier import classify_severity
from pdf_generator import generate_pdf

app = Flask(__name__)
CORS(app)

UPLOAD_FOLDER = 'uploads'
OUTPUT_FOLDER = 'output'

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

model = whisper.load_model("base")

@app.route('/transcribe', methods=['POST'])
def transcribe():
    name = request.form.get('name', 'Unknown')
    transcript = None

    if 'audio' in request.files:
        audio_file = request.files['audio']
        filename = secure_filename(audio_file.filename)
        file_path = os.path.join(UPLOAD_FOLDER, filename)
        audio_file.save(file_path)

        print("[INFO] Transcribing audio...")
        try:
            result = model.transcribe(file_path)
            transcript = result.get('text', '').strip()
            print(f"[INFO] Transcription result: {transcript}")
        except Exception as e:
            print(f"[ERROR] Transcription failed: {e}")
            return jsonify({'error': 'Transcription failed.'}), 500

    elif 'text' in request.form:
        transcript = request.form['text'].strip()
        print("[INFO] Using text input directly.")
    else:
        return jsonify({'error': 'No input provided'}), 400

    if not transcript:
        return jsonify({'error': 'No transcribed text available'}), 400

    severity_level, reasoning = classify_severity(transcript)

    pdf_filename = f"{secure_filename(name)}_report.pdf"
    output_path = os.path.join(OUTPUT_FOLDER, pdf_filename)

    generate_pdf(transcript, severity_level, reasoning, output_path)

    return jsonify({
        'transcript': transcript,
        'severity_level': severity_level,
        'reasoning': reasoning,
        'pdf_url': f'/download/{pdf_filename}'
    })

@app.route('/download/<filename>', methods=['GET'])
def download(filename):
    return send_from_directory(OUTPUT_FOLDER, filename, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
