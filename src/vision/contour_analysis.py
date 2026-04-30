def analyze_contours(features: dict, config: dict) -> tuple[str, float]:
    """
    Analyze contours and detect defect types based on geometric features.
    
    Args:
        features (dict): Dictionary containing 'area' and 'arc_length' keys
        config (dict): Configuration dictionary with 'defect_detection' settings
        
    Returns:
        tuple[str, float]: Defect type ('scratch', 'shape_anomaly', 'missing_component', 'none')
                          and confidence score (0.0-1.0)
                          
    Raises:
        KeyError: If required keys are missing from features or config
    """
    try:
        area = features['area']
        length = features['arc_length']
        detection_config = config['defect_detection']
    except KeyError as e:
        raise KeyError(f"Missing required key: {e}") from e
    
    # Scratch detection
    scratch_max_area = detection_config.get('scratch_max_area', 100)
    scratch_confidence = detection_config.get('scratch_confidence', 0.9)
    if length > detection_config['scratch_min_length'] and area < scratch_max_area:
        return 'scratch', scratch_confidence
    
    # Shape anomaly
    shape_anomaly_confidence = detection_config.get('shape_anomaly_confidence', 0.8)
    if area > detection_config['shape_anomaly_area_threshold']:
        return 'shape_anomaly', shape_anomaly_confidence
    
    # Missing component
    missing_component_confidence = detection_config.get('missing_component_confidence', 0.85)
    min_area, max_area = detection_config['missing_component_area_range']
    if min_area < area < max_area:
        return 'missing_component', missing_component_confidence
    
    return 'none', 0.0
