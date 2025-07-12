from datetime import datetime

def create_response(original_text, translated_text, source_lang, target_lang):
    return {
        "original_text": original_text,
        "translated_text": translated_text,
        "source_language": source_lang,
        "target_language": target_lang,
        "timestamp": datetime.now().isoformat()
    }

def create_error_response(message):
    return {"error": message}
