FROM hashicorp/vault:latest

ENV VAULT_DEV_ROOT_TOKEN_ID=myroot
ENV VAULT_DEV_LISTEN_ADDRESS=0.0.0.0:8200

EXPOSE 8200

CMD ["vault", "server", "-dev", "-dev-root-token-id=myroot", "-dev-listen-address=0.0.0.0:8200"]