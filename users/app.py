from fastapi import FastAPI, HTTPException
from uuid import uuid4
from .models import User
from .db import users_db

app = FastAPI(title="Users Service")

@app.post("/users", response_model=User, status_code=201)
def create_user(payload: User):
    user_id = str(uuid4())
    payload.id = user_id
    users_db[user_id] = payload
    return payload

@app.get("/users/{user_id}", response_model=User)
def get_user(user_id: str):
    user = users_db.get(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="user not found")
    return user

@app.patch("/users/{user_id}", response_model=User)
def update_user(user_id: str, status: str | None = None, credit: float | None = None):
    user = users_db.get(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="user not found")

    if status is not None:
        user.status = status

    if credit is not None:
        if credit < 0:
            raise HTTPException(400, "credit must be >= 0")
        user.credit = credit

    users_db[user_id] = user
    return user

@app.get("/health")
def health():
    return {"status": "ok"}
