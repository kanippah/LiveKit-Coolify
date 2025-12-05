#!/bin/sh
set -e

if [ -z "$LIVEKIT_API_KEY" ] || [ -z "$LIVEKIT_API_SECRET" ]; then
    echo "ERROR: LIVEKIT_API_KEY and LIVEKIT_API_SECRET environment variables must be set"
    exit 1
fi

envsubst < /etc/livekit.yaml.template > /etc/livekit.yaml

exec livekit-server --config /etc/livekit.yaml
