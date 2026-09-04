from fastapi import FastAPI
from e_library_system.controllers.member_controller import router as member_router
from e_library_system.controllers.loan_controller import router as loan_router
from fastapi.middleware.cors import CORSMiddleware
import uvicorn


app = FastAPI(title="E-Library System")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:5500", "http://localhost:5500"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(member_router)
app.include_router(loan_router)

if __name__ == "__main__":
    uvicorn.run("e_library_system.main:app", host="127.0.0.1", port=8000, reload=True)