
# from turtle import title
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes.auth.authRouter import router as api_auth_router

app = FastAPI(
    title="Knowledge management",
    description="An knowledge managent",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],          # Or specify domains: ["http://localhost:3000"]
    allow_credentials=True,
    allow_methods=["*"],          # GET, POST, PUT, DELETE, etc.
    allow_headers=["*"],          # Accept any headers
)

app.include_router(api_auth_router, prefix="/user", tags=["users"])
