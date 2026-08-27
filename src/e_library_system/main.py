from fastapi import FastAPI
from e_library_system.controllers.member_controller import router as member_router


app = FastAPI(title="E-Library System")
app.include_router(member_router)