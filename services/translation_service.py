from googletrans import Translator
from utils.helpers import create_response
from services.logger import log_translation

class TranslationService:
    def __init__(self):
        self.translator = Translator()
    
    def translate_text(self, text, target_language, source_language=None):
        try:
            if source_language:
                result = self.translator.translate(text, dest=target_language, src=source_language)
            else:
                result = self.translator.translate(text, dest=target_language)
            log_translation(text, result.text, result.src, target_language)
            return create_response(text, result.text, result.src, target_language)
        
        except Exception as e:
            raise Exception(f"Translation failed: {str(e)}")
    
    def translate_bulk(self, texts, target_language, source_language=None):
        results = []
        for text in texts:
            try:
                if source_language:
                    result = self.translator.translate(text, dest=target_language, src=source_language)
                else:
                    result = self.translator.translate(text, dest=target_language)

                # Convert to dictionary before appending
                formatted = create_response(text, result.text, result.src, target_language)
                results.append(formatted)
                log_translation(text, result.text, result.src, target_language)

            except Exception as e:
                results.append({"error": str(e), "original_text": text})
        return {"translations": results}