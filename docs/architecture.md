# System Architecture

The Vision Defect Detection System is designed with a modular, extensible architecture for robust industrial quality inspection. Key modules:

- **Preprocessing:** Image normalization, denoising, edge enhancement
- **Defect Detection:** Classical and ML-based methods for scratches, shape anomalies, missing components
- **Contour Analysis:** Shape, area, and geometric feature extraction
- **Feature Extraction:** Statistical and texture features for classification
- **Config Loader:** YAML-based configuration for thresholds and parameters
- **Logging System:** Structured logging with event schema
- **Visualization:** Annotated output images for review

See [system_design.png](system_design.png) for a visual overview.
