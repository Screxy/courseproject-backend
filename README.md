### Create virtual environment

```bash
$ python -m venv venv #(for Linux: python3 -m venv venv)
$ .\venv\Scripts\activate #(for Linux: source ./venv/bin/activate)
```

### Install dependencies

Install dependencies with command `pip install -r requirements.txt`

### Apply migrations

Run  `python manage.py migrate`

### Run project

Run project via `python manage.py runserver`
