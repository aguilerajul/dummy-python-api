# dummy-python-api

This project provides a very small Django API to register events that may
happen during a store day.

## Setup

```bash
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

## Usage

Send a `POST` request to `/actions/` with a JSON body containing an `action`
field. Valid actions are:

- `good_day`
- `street_closed`

Example:

```bash
curl -X POST http://localhost:8000/actions/ -H 'Content-Type: application/json' \
  -d '{"action": "good_day"}'
```
