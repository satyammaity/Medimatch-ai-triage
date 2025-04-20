import datetime

def triage_level(text):
    text = text.lower()

    if "chest pain" in text and ("shortness of breath" in text or "dizzy" in text or "faint" in text):
        return 1
    elif "fever" in text and ("nausea" in text or "dehydration" in text):
        return 2
    elif "abdominal pain" in text or "vomiting" in text:
        return 3
    elif "sprain" in text or "fracture" in text:
        return 4
    elif "refill" in text or "prescription" in text:
        return 5
    else:
        return 3  # Default to moderate if unsure

def create_summary(text):
    level = triage_level(text)
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    return {
        "symptoms": text,
        "triage_level": level,
        "timestamp": timestamp,
        "ai_summary": f"AI suggests triage level {level} based on symptoms"
    }

# Test the function
if __name__ == "__main__":
    input_text = input("Paste patient symptoms: ")
    result = create_summary(input_text)
    print(result)