# LiveKit Self-Hosted Server Configuration

This repository contains the configuration files for deploying a production-ready LiveKit server on Coolify.

## Files

- `Dockerfile` - Custom image that injects credentials at runtime
- `docker-compose.yml` - Docker Compose deployment configuration
- `livekit.yaml.template` - LiveKit config template with environment variable placeholders
- `entrypoint.sh` - Startup script that generates config from environment variables
- `.env.example` - Example environment variables file

## Security

**Credentials are NOT stored in this repository.** The API key and secret are injected at runtime via environment variables, keeping them out of your Git history.

## Required Environment Variables

| Variable | Description |
|----------|-------------|
| `LIVEKIT_API_KEY` | Your LiveKit API key identifier |
| `LIVEKIT_API_SECRET` | Your LiveKit API secret (keep this secure!) |

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

### 4. Set Environment Variables in Coolify

In your Coolify application settings, add these environment variables:

```
LIVEKIT_API_KEY=myApiKey
LIVEKIT_API_SECRET=myVeryLongAndSecureSecretValue123
```

**Generate secure values:**
- API Key: Any identifier you want (e.g., `prod_key`, `my_app`)
- API Secret: Use a long random string (32+ characters recommended)

You can generate a secure secret with:
```bash
openssl rand -base64 32
```

### 5. Configure Domain & SSL

1. In Coolify, go to Domains
2. Add: `livekit.yourdomain.com`
3. Set internal port: `7880`
4. Enable HTTPS via Let's Encrypt

### 6. Firewall Configuration

On your VPS, open the required ports:
```bash
sudo ufw allow 80/tcp
sudo ufw allow 443/tcp
sudo ufw allow 7880/tcp
sudo ufw allow 7881/tcp
sudo ufw allow 50000:60000/udp
```

### 7. Deploy

Click Deploy in Coolify and monitor the logs. You should see:
- Redis starting
- LiveKit server starting with your injected configuration

## Your LiveKit Endpoint

After deployment, your LiveKit server will be accessible at:
```
wss://livekit.yourdomain.com
```

Use this URL along with your API key and secret to connect your applications.

## Port Configuration

| Port | Protocol | Purpose |
|------|----------|---------|
| 7880 | TCP | Main signaling port |
| 7881 | TCP | TCP fallback for signaling |
| 50000-60000 | UDP | Media ports for WebRTC |

## Local Testing (Optional)

To test locally with Docker Compose:

1. Create a `.env` file (copy from `.env.example`):
   ```
   cp .env.example .env
   ```

2. Edit `.env` with your test credentials

3. Run:
   ```bash
   docker-compose up
   ```

**Note:** Never commit your `.env` file to Git!

## Next Steps

After your server is running, you can:
- Build a token generator service (Python, Node.js, PHP)
- Deploy LiveKit Meet UI
- Connect your web/mobile applications
- Integrate AI agents or SIP gateways
