import pytest
from src.pipeline.detection_pipeline import run_detection_pipeline
from src.utils.config_loader import load_config
from src.logging_system.logger import get_logger

def test_pipeline_runs():
    config = load_config('config/config.yaml')
    logger = get_logger(config)
    try:
        run_detection_pipeline(config, logger)
    except Exception as e:
        pytest.fail(f'Pipeline failed: {e}')
