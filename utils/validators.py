from config import SUPPORTED_LANGUAGES, MAX_TEXT_LENGTH, MAX_BULK_SIZE

def validate_text(text):
    if not text or not text.strip():
        raise ValueError("Text cannot be empty")
    if len(text) > MAX_TEXT_LENGTH:
        raise ValueError(f"Text cannot exceed {MAX_TEXT_LENGTH} characters")
    return text.strip()

def validate_language(lang_code):
    if not lang_code or lang_code not in SUPPORTED_LANGUAGES:
        raise ValueError(f"Invalid language. Supported: {list(SUPPORTED_LANGUAGES.keys())}")
    return lang_code

def validate_bulk_texts(texts):
    if not texts or len(texts) > MAX_BULK_SIZE:
        raise ValueError(f"Bulk size must be 1-{MAX_BULK_SIZE}")
    return [validate_text(text) for text in texts]