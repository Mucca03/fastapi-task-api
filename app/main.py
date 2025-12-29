from fastapi import FastAPI
from app.api.routers import auth, task

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}


app.include_router(auth.router)
app.include_router(task.router)