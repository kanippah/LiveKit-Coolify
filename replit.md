# LiveKit Server Configuration Project

## Overview
This is a configuration repository for deploying a self-hosted LiveKit server on Coolify. It contains Docker Compose and LiveKit configuration files that will be deployed to a VPS.

## Purpose
- Store LiveKit server configuration files
- Manage deployment settings via Git
- Push to GitHub for Coolify deployment

## Project Structure
- `livekit.yaml` - LiveKit server configuration
- `docker-compose.yml` - Docker Compose deployment file
- `README.md` - Deployment documentation

## Important Notes
- This is a configuration-only project (no local runtime)
- Files will be pushed to GitHub and pulled by Coolify
- Update API credentials in `livekit.yaml` before deployment
- The server runs on Coolify, not in Replit

## Deployment Target
- Platform: Coolify (Docker Compose)
- Expected endpoint: `wss://livekit.yourdomain.com`
