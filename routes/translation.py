from flask import Blueprint, request, jsonify
from services.translation_service import TranslationService
from utils.validators import validate_text, validate_language, validate_bulk_texts
from utils.helpers import create_error_response
from services.logger import get_logs

bp = Blueprint('translation', __name__)
translation_service = TranslationService()

@bp.route('/translate', methods=['POST'])
def translate():
    try:
        data = request.get_json()
        if not data:
            return jsonify(create_error_response("No JSON data provided")), 400
        
        text = validate_text(data.get('text'))
        target_language = validate_language(data.get('target_language'))
        source_language = data.get('source_language')
        
        result = translation_service.translate_text(text, target_language, source_language)
        return jsonify(result)
    
    except ValueError as e:
        return jsonify(create_error_response(str(e))), 400
    except Exception as e:
        return jsonify(create_error_response(str(e))), 500

@bp.route('/translate/bulk', methods=['POST'])
def translate_bulk():
    try:
        data = request.get_json()
        if not data:
            return jsonify(create_error_response("No JSON data provided")), 400
        
        texts = validate_bulk_texts(data.get('texts', []))
        target_language = validate_language(data.get('target_language'))
        source_language = data.get('source_language')
        
        result = translation_service.translate_bulk(texts, target_language, source_language)
        return jsonify(result)
    
    except ValueError as e:
        return jsonify(create_error_response(str(e))), 400
    except Exception as e:
        return jsonify(create_error_response(str(e))), 500
    
@bp.route('/logs', methods=['GET'])
def get_translation_logs():
    return jsonify({"logs": get_logs()})