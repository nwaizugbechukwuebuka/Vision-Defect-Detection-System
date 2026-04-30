import os
from src.utils.image_loader import load_images
from src.pipeline.preprocessing import preprocess_image
from src.vision.defect_detector import DefectDetector
from src.utils.visualization import save_annotated_image

def run_detection_pipeline(config, logger):
    sample_dir = 'data/samples/'
    output_dir = 'outputs/annotated_images/'

    images = load_images(sample_dir)
    detector = DefectDetector(config)

    for img_path, img in images:
        try:
            preprocessed = preprocess_image(img, config)
            defects, annotated = detector.detect(preprocessed, img)

            save_annotated_image(annotated, img_path, output_dir)

            for defect in defects:
                logger.info("Defect detected", extra=defect)

        except Exception as e:
            logger.error(
                f"Failed on {img_path}: {e}",
                extra={
                    "event_type": "failure",
                    "file": img_path
                }
            )
