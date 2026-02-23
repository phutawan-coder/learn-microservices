from fastapi import FastAPI, HTTPException
import requests
import time

app = FastAPI()

USER_SERVICE = "http://user-service:8000"
MAX_RETRY = 3

@app.post('/orders/{user_id}')
def create_order(user_id: int):
    for i in range(20_000_000):
        pass
    for a in range(MAX_RETRY):
        try:
            res = requests.get(f"{USER_SERVICE}/users/{user_id}", timeout=3) 

            if res.status_code == 200:
                return {"message": "Create order success", "user": res.json()}

            if res.status_code == 404:
                raise HTTPException(status_code=400, detail="User Invalid")

        except requests.exceptions.RequestException:
            print(f"Retry {a}")
            time.sleep(1)
    raise HTTPException(status_code=500, detail="User service unavailable")

@app.get('/health')
def health_check():
    return {"status": "ok"}
