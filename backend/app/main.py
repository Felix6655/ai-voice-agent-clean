from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routers.leads import router as leads_router

app = FastAPI()

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


app.include_router(leads_router)
