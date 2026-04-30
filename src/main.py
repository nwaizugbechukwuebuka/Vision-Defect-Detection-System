from src.pipeline.detection_pipeline import run_detection_pipeline
from src.utils.config_loader import load_config
from src.logging_system.logger import get_logger

def main():
    config = load_config('config/config.yaml')
    logger = get_logger(config)

    logger.info('System startup', extra={'event_type': 'system', 'status': 'startup'})

    try:
        run_detection_pipeline(config, logger)
        logger.info('Pipeline completed', extra={'event_type': 'system', 'status': 'completed'})
    except Exception as e:
        logger.error(
            f'Pipeline failed: {e}',
            extra={'event_type': 'system', 'status': 'error'}
        )

if __name__ == '__main__':
    main()
