# E-Library System Backend

A FastAPI backend for the Bellwood E-Library management system.

## Features

- **Member Management**: Registration, authentication, account status updates.
- **Book Catalogue**: Adding, listing, updating, and removing books.
- **Loan System**: Borrowing and returning books, tracking overdue loans.
- **Librarian Administration**: Staff registration, authentication, and management.

## Tech Stack

- **Framework**: FastAPI
- **Server**: Uvicorn
- **Database**: MySQL (via `mysql-connector-python`)
- **Validation**: Pydantic v2
- **Testing**: Pytest

## Getting Started

### 1. Clone & Set Up Environment

```bash
# Using uv (recommended)
uv sync

# Or using standard venv + pip
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### 2. Configure Database

Set the following environment variables (or rely on defaults for local MySQL):

```bash
export DB_HOST=localhost
export DB_PORT=3306
export DB_USER=root
export DB_PASSWORD=your_password
export DB_NAME=e_library_system

# Or supply a full connection URL:
export DATABASE_URL="mysql://root:password@localhost:3306/e_library_system"
```

### 3. Run the API Server

```bash
uv run uvicorn e_library_system.main:app --reload
```

The interactive API documentation is available at `http://localhost:8000/docs`.

### 4. Run Tests

```bash
uv run pytest src/e_library_system/tests/unit
```

## Deployment to Render

1. Connect this repository to Render as a **Web Service**.
2. **Build Command**: `pip install -r requirements.txt`
3. **Start Command**: `uvicorn e_library_system.main:app --host 0.0.0.0 --port $PORT`
4. Set Environment Variables:
   - `DATABASE_URL`: Connection string to your cloud MySQL instance (e.g. from TiDB Cloud, Aiven, or Railway).
   - `CORS_ORIGINS`: Your Vercel frontend URL (e.g. `https://your-frontend.vercel.app`).
