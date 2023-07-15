# DeepQuarry Backend

The backend for DeepQuarry. Built using FastAPI and PostgreSQL

## Installation

Set your environment variables for Postgres: `APP_USER`, `APP_IP`, and `APP_DB`

Create venv, install deps, init DB  
```
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
chmod +x ./scripts/*
./scripts/resetdb.sh
```

Run the web server  

```
uvicorn app.main:app --reload --port 8000
```

