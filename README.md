# LiveKit Self-Hosted Server Configuration

This repository contains the configuration files for deploying a production-ready LiveKit server on Coolify.

## Files

- `livekit.yaml` - LiveKit server configuration
- `docker-compose.yml` - Docker Compose deployment configuration

## Important: Update API Credentials

Before deploying, you **must** update the API key and secret in `livekit.yaml`:

```yaml
keys:
  YOUR_API_KEY: YOUR_SUPER_SECRET_KEY_VALUE
```

Replace:
- `YOUR_API_KEY` with a unique API key identifier
- `YOUR_SUPER_SECRET_KEY_VALUE` with a long, secure random string

These credentials will be used to generate JWT tokens for your LiveKit clients.

## Deployment Steps

### 1. DNS Configuration
Create an A record pointing to your Coolify server IP:
```
livekit.yourdomain.com → YOUR_SERVER_IP
```

### 2. Push to GitHub
1. Commit these files to your repository
2. Push to GitHub

### 3. Deploy on Coolify
1. Create new Application in Coolify
2. Select Git Repository
3. Enter your GitHub repo URL
4. Set type: **Docker Compose**
5. Set Compose file path: `docker-compose.yml`

### 4. Configure Domain & SSL
1. In Coolify, go to Domains
2. Add: `livekit.yourdomain.com`
3. Set internal port: `7880`
4. Enable HTTPS via Let's Encrypt

### 5. Firewall Configuration
On your VPS, open the required ports:
```bash
sudo ufw allow 80/tcp
sudo ufw allow 443/tcp
sudo ufw allow 7880/tcp
sudo ufw allow 7881/tcp
sudo ufw allow 50000:60000/udp
```

### 6. Deploy
Click Deploy in Coolify and monitor the logs.

## Your LiveKit Endpoint

After deployment, your LiveKit server will be accessible at:
```
wss://livekit.yourdomain.com
```

Use this URL along with your API key and secret to connect your applications.

## Port Configuration

- **7880/tcp** - Main signaling port
- **7881/tcp** - TCP fallback for signaling
- **50000-60000/udp** - Media ports for WebRTC

## Next Steps

After your server is running, you can:
- Build a token generator service (Python, Node.js, PHP)
- Deploy LiveKit Meet UI
- Connect your web/mobile applications
- Integrate AI agents or SIP gateways
