from fastapi import FastAPI
from infra.routers import router

app = FastAPI()
app.include_router(router, prefix="/api")
