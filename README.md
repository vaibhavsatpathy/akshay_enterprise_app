# Accuracy Packaging Management System

Web application for orchestrating daily operations and planning for the corrugation industry. Built with a **FastAPI** backend, **PostgreSQL** database, and a **Streamlit** frontend.
---

## Architecture

| Component  | Technology         | Port  |
|------------|--------------------|-------|
| Backend    | FastAPI (Python)   | 8080  |
| Database   | PostgreSQL 15      | 5432  |
| Frontend   | Streamlit (Python) | 8501  |

The backend and database run together via Docker Compose. The frontend connects to the backend over HTTP.

---

## Prerequisites

### Backend
- [Docker](https://docs.docker.com/get-docker/) v20+
- [Docker Compose](https://docs.docker.com/compose/install/) v2+ (included with Docker Desktop)

### Frontend
- Python 3.8+
- pip

### Windows (additional requirements)
- [Docker Desktop for Windows](https://docs.docker.com/desktop/install/windows-install/) — enables both Docker and Docker Compose v2
- [Git for Windows](https://git-scm.com/download/win) — provides Git Bash, which is required to run the `.sh` helper scripts in `backend/`
- Python from [python.org](https://www.python.org/downloads/) or via `winget install Python.Python.3`
- Run all shell commands in **Git Bash** or **WSL 2** (not PowerShell or CMD), or use the equivalent PowerShell commands in the table below

---

## Setup & Running

### 1. Clone the repository

```bash
git clone <repo-url>
cd akshay_enterprise_app
```

### 2. Backend — Docker

The backend service (FastAPI + PostgreSQL) is fully containerised.

```bash
cd backend

# Build images and start all services in the background
docker compose up -d --build
```

To stop:

```bash
docker compose down
```

To view logs:

```bash
docker compose logs -f
```

> The API will be available at **http://localhost:8080**  
> Interactive API docs (Swagger UI): **http://localhost:8080/docs**

#### Environment variables

Copy and edit the environment file before first run:

```bash
cp backend/core/env_var backend/core/.env
```

Key variables in `docker-compose.yml` that you may want to override:

| Variable    | Default                                                         | Description                          |
|-------------|-----------------------------------------------------------------|--------------------------------------|
| `secret`    | `b9c8e5acc...`                                                  | JWT signing secret — **change this** |
| `algorithm` | `HS256`                                                         | JWT algorithm                        |
| `password`  | `P@ssw0rd`                                                      | Application password                 |
| `db_url`    | `postgresql://postgres:postgres@accuracy_packaging_db:5432/postgres` | PostgreSQL connection URL      |

> **Security:** Never commit real secrets to version control. Set these as environment variables or use a `.env` file (already gitignored).

---

### 3. Frontend — Streamlit

#### Install dependencies

```bash
# macOS / Linux
cd frontend
pip install streamlit pandas requests
```

```powershell
# Windows (PowerShell or Command Prompt)
cd frontend
pip install streamlit pandas requests
```

Or if you prefer a virtual environment:

```bash
# macOS / Linux
python3 -m venv .venv
source .venv/bin/activate
pip install streamlit pandas requests
```

```powershell
# Windows (PowerShell)
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install streamlit pandas requests
```

#### Run the app

```bash
streamlit run main.py --server.port 8501
```

> The UI will be available at **http://localhost:8501**

Make sure the backend is running before starting the frontend.

---

## Project Structure

```
akshay_enterprise_app/
├── backend/
│   ├── docker-compose.yml      # Orchestrates API + DB containers
│   └── core/
│       ├── Dockerfile
│       ├── main.py             # FastAPI entry point
│       ├── requirements.txt    # Python dependencies
│       ├── commons/            # Shared utilities (auth, config, logging)
│       ├── sql/
│       │   ├── apis/           # Route definitions
│       │   ├── controllers/    # Business logic
│       │   ├── crud/           # Database CRUD operations
│       │   └── orm_models/     # SQLAlchemy models
│       └── db/postgres/        # Postgres data volume (gitignored)
└── frontend/
    ├── main.py                 # Streamlit entry point
    ├── commons/                # API helpers, UI utilities
    └── pages/                  # Multi-page Streamlit app
        ├── 1_👥_User_Management.py
        ├── 2_📏_Master_Data.py
        ├── 3_🏢_Lookup_Tables.py
        ├── 4_📦_Inventory.py
        ├── 5_🖨️_Printing.py
        ├── 6_📋_Orders_Die.py
        ├── 7_⚙️_Jobs.py
        └── 8_🚚_Dispatch.py
```

---

## Useful Commands

### macOS / Linux

| Action                        | Command                                          |
|-------------------------------|--------------------------------------------------|
| Start backend (detached)      | `cd backend && docker compose up -d`             |
| Rebuild after code changes    | `cd backend && docker compose up -d --build`     |
| Stop backend                  | `cd backend && docker compose down`              |
| View backend logs             | `cd backend && docker compose logs -f`           |
| Start frontend                | `cd frontend && streamlit run main.py`           |
| Reset DB (⚠️ deletes all data) | `cd backend && docker compose down -v`           |

### Windows (PowerShell or Command Prompt)

| Action                        | Command                                                    |
|-------------------------------|------------------------------------------------------------|
| Start backend (detached)      | `cd backend; docker compose up -d`                         |
| Rebuild after code changes    | `cd backend; docker compose up -d --build`                 |
| Stop backend                  | `cd backend; docker compose down`                          |
| View backend logs             | `cd backend; docker compose logs -f`                       |
| Start frontend                | `cd frontend; streamlit run main.py`                       |
| Reset DB (⚠️ deletes all data) | `cd backend; docker compose down -v`                       |

> **Windows tip:** The `./start_all.sh`, `./stop_all.sh`, and `./restart_all.sh` convenience scripts in `backend/` are Bash scripts. On Windows, run them inside **Git Bash** or **WSL 2**, or use the equivalent `docker compose` commands from the table above directly in PowerShell.

> **Docker CLI version:** Docker Desktop v2+ ships `docker compose` (with a space) as a built-in plugin. If you have an older standalone install that provides `docker-compose` (with a hyphen), both work identically — use whichever is available on your system.
