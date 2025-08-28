# flask-ci-demo

Minimal Flask project with a simple frontend form, built with a CI pipeline (no tests, no deploy).

## Run locally (Ubuntu)
```
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
flask --app app.routes run --reload```
