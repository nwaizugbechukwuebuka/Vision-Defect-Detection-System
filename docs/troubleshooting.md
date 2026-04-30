# Troubleshooting Guide

## Common Issues
- **No defects detected:**
  - Check config thresholds in `config/config.yaml`
  - Ensure sample images are in `data/samples/`
- **Pipeline errors:**
  - Review logs in `outputs/logs/system.log`
  - Validate YAML syntax
- **Poor detection accuracy:**
  - Adjust preprocessing or detection parameters
  - Use higher quality sample images

## Logging
All system events and errors are logged in `outputs/logs/system.log`.
