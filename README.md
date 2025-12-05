# LiveKit Server

Production-ready LiveKit WebRTC server on Coolify.

## Files

- `docker-compose.yml` - Main deployment config
- `livekit.yaml` - LiveKit server configuration
- `caddy.yaml` - HTTPS/reverse proxy (auto TLS)
- `redis.conf` - Redis cache configuration
- `.env.example` - Example environment variables

## Setup

### 1. Update domain in caddy.yaml
Replace `livekit.koaditech.com` with your domain:
```yaml
- host: ["your-domain.com"]
```

### 2. Update email in caddy.yaml
Replace with your email for Let's Encrypt certificates:
```yaml
email: your-email@your-domain.com
```

### 3. Point DNS
Create DNS A record:
```
your-domain.com → YOUR_SERVER_IP
```

### 4. Deploy to Coolify
1. Push to GitHub
2. Create Docker Compose app in Coolify
3. Set compose file: `docker-compose.yml`
4. Deploy

## Your Endpoint

```
wss://your-domain.com
```

Use API key/secret to generate JWT tokens:
```
API Key: livekit_2687edd1c05cfb2b
API Secret: ONqu0KkPr6P625PxAR7ovlXbeekGod43oFku2DpI2g8
```

## Firewall Ports

Open these on your VPS:
- `80/tcp` - HTTP (TLS issuance)
- `443/tcp` - HTTPS (WebSocket)
- `443/udp` - TURN/UDP
- `7881/tcp` - WebRTC over TCP
- `50000-60000/udp` - WebRTC media

## Monitoring

Check logs on VPS:
```bash
docker compose logs livekit
docker compose logs caddy
```

## Generate New API Keys

```bash
openssl rand -base64 32
```
