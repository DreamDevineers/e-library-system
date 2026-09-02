from fastapi import FastAPI
from e_library_system.controllers.member_controller import router as member_router
from e_library_system.controllers.loan_controller import router as loan_router
import uvicorn

app = FastAPI(title="E-Library System")
app.include_router(member_router)
app.include_router(loan_router)

if __name__ == "__main__":
    uvicorn.run("e_library_system.main:app", host="127.0.0.1", port=8000, reload=True)