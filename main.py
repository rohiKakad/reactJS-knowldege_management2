from contextlib import asynccontextmanager

# from turtle import title
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.controller.authController import AuthController
from app.routes.auth.authRouter import router as api_auth_router
from app.routes.forms.formsRouter import router as api_forms_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    print("🔄 App starting up...")
    yield  # ← this is where the app runs
    print("🛑 App shutting down...")
    controller.close_connection()
app = FastAPI(
    title="Knowledge management",
    description="An knowledge managent",
    version="1.0.0",
    lifespan=lifespan
)

controller = AuthController()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],          # Or specify domains: ["http://localhost:3000"]
    allow_credentials=True,
    allow_methods=["*"],          # GET, POST, PUT, DELETE, etc.
    allow_headers=["*"],          # Accept any headers
)

app.include_router(api_auth_router, prefix="/user", tags=["users"])
app.include_router(api_forms_router, prefix="/forms", tags=["forms"])
