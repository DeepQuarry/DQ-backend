# DeepQuarry Backend

The backend for DeepQuarry. Built using FastAPI, PostgreSQL, and AWS API Gateway. Deployed with Heroku and AWS S3.

## Installation

### Env vars

Set your environment variables. Note that beacuse the prod server uses `DATABASE_URL`, it is not necessary to provide it here. The `Postgres_xxx..` variables will create the dev DB url automatically.

If both are provided, `DATABASE_URL` will take priority.

| VAR  | DESC | OPTIONAL |
| ------------- | ------------- | ------------- |
| API_KEY  | Bearer Token to access the API  | no |
| AWS_ACCESS_KEY_ID  | AWS access key  | no |
| AWS_SECRET_ACCESS_KEY | AWS secret key | no |
| AWS_BUCKET | S3 bucket name | yes |
| DATABASE_URL | URL to PostgreSQL DB | yes |
| POSTGRES_USER | DB user | no |
| POSTGRES_PASSWORD | DB password | yes |
| POSTGRES_IP | DB IP | no |
| POSTGRES_PORT | DB port | yes |
| POSTGRES_DB | DB name | no |
| TESTING | Specify testing mode | yes |


### Setup dev

```bash
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

## Public API Usage
The API is currently hosted at `https://deepquarry-28dd5496b5af.herokuapp.com/api/v1`.

[Documentation](https://deepquarry-28dd5496b5af.herokuapp.com/docs)

**When sending a request, supply the API Key in the form of Bearer Token authentication.

### Example
```python
import requests
endpoint = "https://deepquarry-28dd5496b5af.herokuapp.com/v1/api/query"
query = {"query": "munchkin cat", "threads": 5, "image_limit": 100}
API_KEY = os.getenv("API_KEY")
headers = {"Authorization": f"Bearer {API_KEY}"}
response = requests.post(endpoint, data=query, headers=headers).json()
```

