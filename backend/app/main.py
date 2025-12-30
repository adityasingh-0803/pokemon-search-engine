from fastapi import FastAPI
from app.api import router

app = FastAPI(
    title="Pokemon Search Engine API",
    version="1.0.0"
)

app.include_router(router)

@app.get("/")
def health():
    return {"status": "running"}
