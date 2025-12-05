# LiveKit Server on Coolify

Deploy a production LiveKit server using Coolify.

## Setup

### 1. DNS
Create an A record:
```
livekit.yourdomain.com → YOUR_SERVER_IP
```

### 2. Environment Variables in Coolify
Set these in Coolify:
```
LIVEKIT_API_KEY=livekit_2687edd1c05cfb2b
LIVEKIT_API_SECRET=ONqu0KkPr6P625PxAR7ovlXbeekGod43oFku2DpI2g8
```

### 3. Deploy
Push to GitHub, then in Coolify:
- Create new Docker Compose app
- Set compose file path: `docker-compose.yml`
- Set domain: `livekit.yourdomain.com`
- Enable HTTPS
- Deploy

## Your Endpoint

```
wss://livekit.yourdomain.com
```

Use the API key and secret to generate JWT tokens for your clients.

## Ports

- 7880: Signaling (TCP)
- 7881: Signaling fallback (TCP)
- 50000-60000: Media (UDP)

## Firewall

Open these ports on your VPS:
```bash
sudo ufw allow 80/tcp
sudo ufw allow 443/tcp
sudo ufw allow 7880/tcp
sudo ufw allow 7881/tcp
sudo ufw allow 50000:60000/udp
```
