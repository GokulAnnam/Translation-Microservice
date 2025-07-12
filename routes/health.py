from flask import Blueprint, jsonify
from datetime import datetime

bp = Blueprint('health', __name__)

@bp.route('/health', methods=['GET'])
def health():
    try:
        return jsonify({
            "status": "healthy",
            "timestamp": datetime.now().isoformat(),
            "service": "translation-microservice"
        })
    except Exception as e:
        return jsonify({
            "status": "unhealthy",
            "reason": str(e),
            "timestamp": datetime.now().isoformat()
        }), 503