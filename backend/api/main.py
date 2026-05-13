from fastapi import FastAPI
from backend.api.routes import router

app = FastAPI(title="Banking AI Copilot API")

app.include_router(router, prefix="/api")

if __name__ == "__main__":
    import uvicorn
    from backend.core.config import settings
    uvicorn.run(app, host=settings.HOST, port=settings.PORT)
