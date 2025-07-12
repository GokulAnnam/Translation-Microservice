from flask import Flask
from routes.translation import bp as translation_bp
from routes.health import bp as health_bp

def create_app():
    app = Flask(__name__)
    
    # Register blueprints
    app.register_blueprint(translation_bp, url_prefix='/api/v1')
    app.register_blueprint(health_bp)
    
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', port=5000, debug=True)