import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

from e_library_system.controllers.member_controller import router as member_router
from e_library_system.controllers.loan_controller import router as loan_router
from e_library_system.controllers.librarian_controller import router as librarian_router
from e_library_system.controllers.book_controller import router as book_router


app = FastAPI(
    title="E-Library System API",
    description="Backend services for the Bellwood E-Library application",
    version="1.0.0",
)

# Configure CORS for local development and live deployments (Vercel, Render)
raw_origins = os.getenv("CORS_ORIGINS", "http://localhost:5173,http://localhost:3000,http://127.0.0.1:5173")
origins = [origin.strip() for origin in raw_origins.split(",") if origin.strip()]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins if "*" not in origins else ["*"],
    allow_origin_regex=r"https://.*\.vercel\.app" if "*" not in origins else None,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(member_router)
app.include_router(loan_router)
app.include_router(librarian_router)
app.include_router(book_router)


@app.get("/")
def root():
    return {
        "status": "online",
        "service": "E-Library System API",
        "docs": "/docs",
    }


@app.get("/health")
def health():
    return {"status": "ok"}


if __name__ == "__main__":
    port = int(os.getenv("PORT", 8000))
    uvicorn.run("e_library_system.main:app", host="0.0.0.0", port=port, reload=True)
