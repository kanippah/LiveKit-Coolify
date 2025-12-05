# LiveKit Server Configuration Project

## Overview
This is a configuration repository for deploying a self-hosted LiveKit server on Coolify. It contains Docker Compose and LiveKit configuration files that will be deployed to a VPS.

## Purpose
- Store LiveKit server configuration files
- Manage deployment settings via Git
- Push to GitHub for Coolify deployment

## Project Structure
```
├── Dockerfile              # Custom image with credential injection
├── docker-compose.yml      # Docker Compose deployment file
├── livekit.yaml.template   # Config template with env var placeholders
├── entrypoint.sh           # Startup script that generates config
├── .env.example            # Example environment variables
├── validate_config.py      # Configuration validation script
└── README.md               # Deployment documentation
```

## Security Model
Credentials are injected at runtime via environment variables:
- `LIVEKIT_API_KEY` - API key identifier
- `LIVEKIT_API_SECRET` - Secret value for token generation

These are set in Coolify, NOT in the repository.

## Validation
Run `python validate_config.py` to check all configuration files.

## Deployment Target
- Platform: Coolify (Docker Compose)
- Expected endpoint: `wss://livekit.yourdomain.com`

## Important Notes
- Never commit `.env` files
- Set credentials in Coolify environment variables
- The livekit.yaml is generated at container startup from the template
