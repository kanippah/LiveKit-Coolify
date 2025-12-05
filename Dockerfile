FROM livekit/livekit-server:latest

RUN apk add --no-cache gettext

COPY livekit.yaml.template /etc/livekit.yaml.template
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]
