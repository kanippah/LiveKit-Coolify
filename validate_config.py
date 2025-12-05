#!/usr/bin/env python3
"""
LiveKit Configuration Validator

This script validates that the configuration files are properly formatted
and ready for deployment to Coolify.
"""

import yaml
import sys
from pathlib import Path

def validate_yaml_file(filepath):
    """Validate a YAML file exists and can be parsed."""
    try:
        with open(filepath, 'r') as f:
            data = yaml.safe_load(f)
        print(f"✓ {filepath} is valid YAML")
        return True, data
    except FileNotFoundError:
        print(f"✗ {filepath} not found")
        return False, None
    except yaml.YAMLError as e:
        print(f"✗ {filepath} has YAML syntax errors: {e}")
        return False, None

def check_livekit_config(data):
    """Check LiveKit configuration for required fields."""
    issues = []
    
    if not data:
        return ["Configuration is empty"]
    
    if 'port' not in data:
        issues.append("Missing 'port' field")
    
    if 'keys' not in data:
        issues.append("Missing 'keys' field")
    elif isinstance(data['keys'], dict):
        if 'PROD_API_KEY' in data['keys'] and data['keys']['PROD_API_KEY'] == 'PROD_SUPER_SECRET_KEY_VALUE':
            issues.append("⚠ WARNING: Using default API credentials! Update before deployment.")
    
    if 'rtc' not in data:
        issues.append("Missing 'rtc' configuration")
    
    return issues

def check_docker_compose(data):
    """Check Docker Compose configuration."""
    issues = []
    
    if not data:
        return ["Configuration is empty"]
    
    if 'services' not in data:
        issues.append("Missing 'services' field")
    else:
        services = data['services']
        if 'livekit' not in services:
            issues.append("Missing 'livekit' service")
        if 'redis' not in services:
            issues.append("Missing 'redis' service")
    
    return issues

def main():
    print("=" * 60)
    print("LiveKit Configuration Validator")
    print("=" * 60)
    print()
    
    all_valid = True
    
    # Validate livekit.yaml
    print("Checking livekit.yaml...")
    valid, livekit_data = validate_yaml_file('livekit.yaml')
    if valid:
        issues = check_livekit_config(livekit_data)
        if issues:
            for issue in issues:
                print(f"  {issue}")
            if any('WARNING' not in issue for issue in issues):
                all_valid = False
    else:
        all_valid = False
    print()
    
    # Validate docker-compose.yml
    print("Checking docker-compose.yml...")
    valid, compose_data = validate_yaml_file('docker-compose.yml')
    if valid:
        issues = check_docker_compose(compose_data)
        if issues:
            for issue in issues:
                print(f"  {issue}")
            all_valid = False
    else:
        all_valid = False
    print()
    
    # Check if README exists
    print("Checking README.md...")
    if Path('README.md').exists():
        print("✓ README.md exists")
    else:
        print("✗ README.md not found")
        all_valid = False
    print()
    
    # Final summary
    print("=" * 60)
    if all_valid:
        print("✓ All configuration files are valid!")
        print()
        print("Next steps:")
        print("1. Update API credentials in livekit.yaml")
        print("2. Commit and push to GitHub")
        print("3. Deploy on Coolify")
        print("=" * 60)
        return 0
    else:
        print("✗ Configuration has errors. Please fix them before deployment.")
        print("=" * 60)
        return 1

if __name__ == "__main__":
    sys.exit(main())
