import whisper
import os

def transcribe_audio(file_path):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Audio file not found: {file_path}")

    print("[INFO] Loading Whisper model...")
    model = whisper.load_model("base")

    print("[INFO] Transcribing...")
    result = model.transcribe(file_path)

    print("[INFO] Transcription complete.")
    return result["text"]