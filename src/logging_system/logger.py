import logging
import os
from src.logging_system.event_schema import EventAdapter

def get_logger(config):
    log_path = config['logging']['log_file']
    os.makedirs(os.path.dirname(log_path), exist_ok=True)

    logger = logging.getLogger('vision_system')
    logger.setLevel(getattr(logging, config['logging']['log_level']))

    # Prevent duplicate handlers (VERY IMPORTANT)
    if not logger.handlers:
        fh = logging.FileHandler(log_path)

        formatter = logging.Formatter(
            '%(asctime)s | %(levelname)s | %(message)s'
        )

        fh.setFormatter(formatter)
        logger.addHandler(fh)

    return EventAdapter(logger, {})
