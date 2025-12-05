#!/bin/sh
set -e

if [ -z "$LIVEKIT_API_KEY" ] || [ -z "$LIVEKIT_API_SECRET" ]; then
    echo "ERROR: LIVEKIT_API_KEY and LIVEKIT_API_SECRET environment variables must be set"
    exit 1
fi

# Generate config from template using sed instead of envsubst (more portable)
sed "s|\${LIVEKIT_API_KEY}|$LIVEKIT_API_KEY|g; s|\${LIVEKIT_API_SECRET}|$LIVEKIT_API_SECRET|g" \
    /etc/livekit.yaml.template > /etc/livekit.yaml

exec livekit-server --config /etc/livekit.yaml
