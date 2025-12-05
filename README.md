# LiveKit Server on Coolify

Production LiveKit deployment on Coolify with automatic reverse proxy & HTTPS.

## Files

- `docker-compose.yaml` - Services only (Coolify handles routing)
- `livekit.yaml` - LiveKit server config
- `redis.conf` - Redis cache
- `README.md` - This file

## Setup in Coolify

1. **Create Docker Compose Application**
   - Paste repo URL: `https://github.com/kanippah/LiveKit-Coolify`
   - Compose file: `docker-compose.yaml`
   - Build pack: Raw Docker Compose (no build needed)

2. **Set Domain**
   - Domain: `livekit.koaditech.com`
   - Coolify auto-creates HTTPS via Let's Encrypt

3. **Configure Ports** (in Coolify)
   - Container port: 7880
   - Public port: 443
   - Protocol: WebSocket

4. **Deploy**
   - Click Deploy
   - Monitor logs

## Your Endpoint

```
wss://livekit.koaditech.com
```

## API Credentials

```
API Key: livekit_2687edd1c05cfb2b
API Secret: ONqu0KkPr6P625PxAR7ovlXbeekGod43oFku2DpI2g8
```

## Network Requirements

Ensure these ports are open on your VPS:
- `443/tcp` - HTTPS (Coolify proxy)
- `50000-60000/udp` - WebRTC media

## Generate New Keys

```bash
openssl rand -base64 32
```
