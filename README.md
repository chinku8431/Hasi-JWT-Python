uvicorn main:app --reload  --backend


python -m http.server 8080  --front end run

http://127.0.0.1:8080/index.html ---frontend open in browser

2//

Set Up HashiCorp Vault

Start the vault

vault server -dev

Set Vault Token in Environment Variables: Export the root token to the environment variable VAULT_TOKEN:

export VAULT_TOKEN=<root_token> 

Store Secrets in Vault:----------

Login to vault

vault login $VAULT_TOKEN

write the secret

vault kv put secret/my-app/credentials username=admin password=admin123

3//
Environment Variables

Vault Token:

export VAULT_TOKEN=<your_vault_token>

Secret Key for JWT: Replace your_secret_key in the code with a secure key or set it as an environment variable:

export SECRET_KEY="your_secure_key"

Test :: 
Vault URL: Ensure the Vault server URL (http://127.0.0.1:8200) is reachable from the application.

4//Start the FastAPI Application

uvicorn <filename>:app --reload

Replace <filename> with your script's filename (e.g., main.py).

5//Test the Application

a//Generate a JWT Token: Use a tool like python-jose or any JWT generator to create a token using HS256 and the secret key:

from jose import jwt

SECRET_KEY = "your_secret_key"
ALGORITHM = "HS256"

token = jwt.encode({"sub": "test_user"}, SECRET_KEY, algorithm=ALGORITHM)
print(token)

b//Test Upload Endpoint: Use a tool like Postman or curl to test the /compare-files/ endpoint:

curl -X POST "http://127.0.0.1:8000/compare-files/" \
-H "Authorization: Bearer <your_jwt_token>" \
-F "file1=@path/to/file1.txt" \
-F "file2=@path/to/file2.txt"

