from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routers.leads import router as leads_router
from app.routers.voice import router as voice_router

app = FastAPI(title="AI Voice Agent Clean")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def root():
    return {"status": "running"}


@app.get("/api/health")
def health():
    return {"ok": True}


app.include_router(leads_router, prefix="/api")
app.include_router(voice_router, prefix="/api")