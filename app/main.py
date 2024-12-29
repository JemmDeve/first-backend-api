from fastapi import FastAPI
from app.routes import tasks

app = FastAPI()

# Registrar las rutas
app.include_router(tasks.router, prefix="/api", tags=["Tasks"])
