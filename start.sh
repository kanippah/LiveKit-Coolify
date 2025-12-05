#!/bin/bash
set -e

echo "Starting LiveKit with environment variables..."
echo "LIVEKIT_API_KEY=${LIVEKIT_API_KEY}"
echo "LIVEKIT_API_SECRET=${LIVEKIT_API_SECRET}"

if [ -z "$LIVEKIT_API_KEY" ] || [ -z "$LIVEKIT_API_SECRET" ]; then
    echo "ERROR: LIVEKIT_API_KEY and LIVEKIT_API_SECRET environment variables must be set"
    exit 1
fi

echo "Generating config from template..."
cat /etc/livekit.yaml.template | \
    sed "s|\${LIVEKIT_API_KEY}|${LIVEKIT_API_KEY}|g" | \
    sed "s|\${LIVEKIT_API_SECRET}|${LIVEKIT_API_SECRET}|g" > /etc/livekit.yaml

echo "Generated config:"
cat /etc/livekit.yaml

echo "Starting livekit-server..."
exec livekit-server --config /etc/livekit.yaml
