from fastapi import FastAPI

app = FastAPI()

users = {
            1: {"id": 1, "name": "phutawan"},
            2: {"id": 2, "name": "siriprang"}
        }

@app.get('/users/{user_id}')
def get_user(user_id: int):
    user = users.get(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    else: 
        return user

@app.get('/health')
def health_check():
    return {"status": "ok"}
