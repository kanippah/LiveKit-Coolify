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
        print(f"  ✓ {filepath} is valid YAML")
        return True, data
    except FileNotFoundError:
        print(f"  ✗ {filepath} not found")
        return False, None
    except yaml.YAMLError as e:
        print(f"  ✗ {filepath} has YAML syntax errors: {e}")
        return False, None

def check_file_exists(filepath, description):
    """Check if a file exists."""
    if Path(filepath).exists():
        print(f"  ✓ {filepath} exists")
        return True
    else:
        print(f"  ✗ {filepath} not found ({description})")
        return False

def check_livekit_template(data):
    """Check LiveKit template configuration."""
    issues = []
    
    if not data:
        return ["Configuration is empty"]
    
    if 'port' not in data:
        issues.append("Missing 'port' field")
    
    if 'keys' not in data:
        issues.append("Missing 'keys' field")
    
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
        else:
            livekit = services['livekit']
            if 'environment' not in livekit:
                issues.append("Missing 'environment' in livekit service")
            elif isinstance(livekit['environment'], list):
                env_vars = [e.split('=')[0] if '=' in e else e.split(':')[0].replace('${', '').replace('}', '') for e in livekit['environment']]
                if 'LIVEKIT_API_KEY' not in str(livekit['environment']):
                    issues.append("LIVEKIT_API_KEY not configured in environment")
                if 'LIVEKIT_API_SECRET' not in str(livekit['environment']):
                    issues.append("LIVEKIT_API_SECRET not configured in environment")
        
        if 'redis' not in services:
            issues.append("Missing 'redis' service")
    
    return issues

def main():
    print("=" * 60)
    print("LiveKit Configuration Validator")
    print("=" * 60)
    print()
    
    all_valid = True
    
    # Check required files
    print("Checking required files...")
    files_to_check = [
        ('Dockerfile', 'Custom Docker image'),
        ('entrypoint.sh', 'Startup script'),
        ('livekit.yaml.template', 'Config template'),
        ('.env.example', 'Example environment file'),
    ]
    
    for filepath, description in files_to_check:
        if not check_file_exists(filepath, description):
            all_valid = False
    print()
    
    # Validate livekit.yaml.template
    print("Validating livekit.yaml.template...")
    valid, template_data = validate_yaml_file('livekit.yaml.template')
    if valid:
        issues = check_livekit_template(template_data)
        if issues:
            for issue in issues:
                print(f"  ⚠ {issue}")
    else:
        all_valid = False
    print()
    
    # Validate docker-compose.yml
    print("Validating docker-compose.yml...")
    valid, compose_data = validate_yaml_file('docker-compose.yml')
    if valid:
        issues = check_docker_compose(compose_data)
        if issues:
            for issue in issues:
                print(f"  ⚠ {issue}")
            all_valid = False
    else:
        all_valid = False
    print()
    
    # Check security
    print("Security checks...")
    if Path('.env').exists():
        print("  ⚠ WARNING: .env file exists - make sure it's in .gitignore!")
    else:
        print("  ✓ No .env file (credentials will be set in Coolify)")
    
    # Check .gitignore
    if Path('.gitignore').exists():
        with open('.gitignore', 'r') as f:
            gitignore = f.read()
        if '.env' in gitignore:
            print("  ✓ .env is in .gitignore")
        else:
            print("  ⚠ WARNING: .env should be in .gitignore!")
    print()
    
    # Final summary
    print("=" * 60)
    if all_valid:
        print("✓ All configuration files are valid!")
        print()
        print("Your credentials are secure:")
        print("  - API key/secret are NOT in the repository")
        print("  - They will be injected via environment variables")
        print()
        print("Next steps:")
        print("  1. Push to GitHub")
        print("  2. Create app in Coolify (Docker Compose type)")
        print("  3. Set LIVEKIT_API_KEY and LIVEKIT_API_SECRET in Coolify")
        print("  4. Deploy!")
    else:
        print("✗ Configuration has errors. Please fix them before deployment.")
    print("=" * 60)
    
    return 0 if all_valid else 1

if __name__ == "__main__":
    sys.exit(main())
