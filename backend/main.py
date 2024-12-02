from fastapi import FastAPI, File, UploadFile, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
import os
import hvac

# Configurations
app = FastAPI()
SECRET_KEY = "your_secret_key"
ALGORITHM = "HS256"

# OAuth2 for JWT
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# HashiCorp Vault Client
def get_vault_secret():
    client = hvac.Client(url="http://127.0.0.1:8200")
    client.token = os.getenv("VAULT_TOKEN")
    secret = client.secrets.kv.read_secret_version(path="my-app/credentials")
    return secret["data"]["data"]

def verify_token(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")

@app.post("/compare-files/")
async def compare_files(
    file1: UploadFile = File(...), file2: UploadFile = File(...), token: str = Depends(verify_token)
):
    # Read file content
    content1 = (await file1.read()).decode("utf-8")
    content2 = (await file2.read()).decode("utf-8")

    # Compare files word-by-word
    diff = []
    for word1, word2 in zip(content1.split(), content2.split()):
        if word1 != word2:
            diff.append((word1, word2))

    return {"differences": diff}
