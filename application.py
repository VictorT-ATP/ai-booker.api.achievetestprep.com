from flask import Flask
from dotenv import load_dotenv
from logging.config import dictConfig
import logging
import os

load_dotenv()

dictConfig(
    {
        "version": 1,
        "formatters": {
            "default": {
                "format": "[%(asctime)s] %(levelname)s > %(module)s: %(message)s",
            }
        },
        "handlers": {
            "console": {
                "class": "logging.StreamHandler",
                "stream": "ext://sys.stdout",
                "formatter": "default",
            },
            "file": {
                "class": "logging.handlers.RotatingFileHandler",
                "filename": "log/app.log",
                "maxBytes": 1000000,
                "backupCount": 10,
                "formatter": "default",
            },
        },
        "root": {"level": "DEBUG", "handlers": ["console", "file"]},
    }
)

def create_app():
    app = Flask(__name__)
    app.logger.setLevel(logging.DEBUG if os.getenv(
        "FLASK_DEBUG", "true").lower() == "true" else logging.INFO)

    # Register

    # features: Home
    from features.home import home_bp

    app.register_blueprint(home_bp, url_prefix='/')

    # features: Leads
    from features.leads import leads_bp
    app.register_blueprint(leads_bp, url_prefix='/leads')

    # features: Batch Service
    from features.batch_service import batch_service_bp
    app.register_blueprint(batch_service_bp, url_prefix='/batch_service')

    # features: Manual Execution
    from features.manual_exec import manual_exec_bp
    app.register_blueprint(manual_exec_bp, url_prefix='/manual_exec')

    # features: Calls Log
    from features.conversations_log import conversations_log_bp
    app.register_blueprint(conversations_log_bp, url_prefix='/conversations_log')

    # features: Analytics
    from features.statistics import statistics_bp
    app.register_blueprint(statistics_bp, url_prefix='/statistics')

    from features.settings import settings_bp
    app.register_blueprint(settings_bp, url_prefix='/settings')

    return app

if __name__ == "__main__":
    main_app = create_app()
    main_app.run(port=8000)