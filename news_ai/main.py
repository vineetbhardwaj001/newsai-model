from fastapi import FastAPI
from app.api.routes import router
from app import initialize_app

app = FastAPI(
    title="News AI API",
    version="1.0",
    description="AI-powered News Analysis System"
)

# Initialize app
initialize_app()

# Include routes
app.include_router(router)