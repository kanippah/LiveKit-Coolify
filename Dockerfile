FROM livekit/livekit-server:latest

COPY livekit.yaml.template /etc/livekit.yaml.template
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]
