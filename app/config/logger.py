import os
from logging.config import dictConfig


def configure_logging(app):
    # Create logs directory if it doesn't exist
    if not os.path.exists('logs'):
        os.makedirs('logs')

    logging_config = dict(
        version=1,
        formatters={
            'default': {
                'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
            },
        },
        handlers={
            'console': {
                'class': 'logging.StreamHandler',
                'formatter': 'default',
            },
            'file': {
                'class': 'logging.handlers.RotatingFileHandler',
                'filename': os.path.join('logs', 'app.log'),
                'maxBytes': 10240,
                'backupCount': 10,
                'formatter': 'default',
            },
        },
        root={
            'level': app.config['LOG_LEVEL'],
            'handlers': ['console', 'file']
        },
    )

    dictConfig(logging_config)