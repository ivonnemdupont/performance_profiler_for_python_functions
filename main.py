from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": "¡Hola, mundo!"}

@app.get("/users/{user_id}")
async def read_user(user_id: int):
    return {"user_id": user_id}
