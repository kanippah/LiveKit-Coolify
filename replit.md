# LiveKit Server Production Deployment

Deploying LiveKit WebRTC server on Coolify with automatic TLS via Caddy.

## Current Setup
- **Config**: Official LiveKit generator format
- **Caddy**: Reverse proxy + automatic HTTPS via Let's Encrypt
- **Redis**: Cache/state management
- **Domain**: livekit.koaditech.com (update as needed)
- **API Key**: livekit_2687edd1c05cfb2b
- **API Secret**: ONqu0KkPr6P625PxAR7ovlXbeekGod43oFku2DpI2g8

## Files
- `docker-compose.yml` - Main deployment
- `livekit.yaml` - LiveKit config
- `caddy.yaml` - Reverse proxy config
- `redis.conf` - Redis config
- `README.md` - Deployment instructions

## Next Steps
1. Update domain in `caddy.yaml`
2. Update email in `caddy.yaml`
3. Point DNS to server IP
4. Push to GitHub
5. Deploy in Coolify
