from datetime import datetime
import json

translation_logs = []
LOG_FILE = "translation_logs.txt"

def log_translation(original_text, translated_text, source_lang, target_lang):
    log_entry = {
        "timestamp": datetime.now().isoformat(),
        "original_text": original_text,
        "translated_text": translated_text,
        "source_language": source_lang,
        "target_language": target_lang
    }

    # Store in-memory
    translation_logs.append(log_entry)

    #write to file
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(json.dumps(log_entry, ensure_ascii=False) + "\n")

def get_logs():
    return translation_logs
