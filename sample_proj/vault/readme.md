1. Create Docker file content (staged to git)
2. docker build -t vault-dev-image  .
3. docker run --cap-add=IPC_LOCK -p 8200:8200 --name vault-dev vault-dev-image 
4. while running : docker stop vault-dev 
5. while stopped : docker start vault-dev 
6. Open your browser and go to: http://localhost:8200 (Use root token: myroot)


Add / Pull keys via the Vault CLI (recommended if you have the CLI installed):
1. export VAULT_ADDR='http://127.0.0.1:8200' 
2. export VAULT_TOKEN='myroot'
3. vault kv put secret/PATH username=admin password=supersecret 
4. vault kv get -version=X secret/PATH


Add / Pull keys via HTTP API (no CLI required):
1. (write): curl --header "X-Vault-Token: myroot" \
     --request POST \
     --data '{"data": {"username": "admin", "password": "supersecret"}}' \
     http://127.0.0.1:8200/v1/secret/data/myapp
2. (read): curl --header "X-Vault-Token: myroot" \
     http://127.0.0.1:8200/v1/secret/data/myapp 






** Docker compose for persistent storage **
1. create new image with : docker compose up 
2. docker exec -it local_vault vault operator init    

3. docker exec -it local_vault vault operator unseal  # repeat 3 times with unseal keys (1-3)
4. http://localhost:8200