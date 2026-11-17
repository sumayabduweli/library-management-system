<<<<<<< HEAD
# Library Management System

## Group Members

- Kasasa Hajara — 224-063011-29919
- Nabukenya Shifra — 224-063011-29636
- Sumaya Abduweli — 224-063011-29621

## Run on Windows

1. Install Python 3.12 or newer and make sure `py` works in PowerShell.
2. Open PowerShell in this folder (the folder containing `manage.py`).
3. Create and activate a virtual environment:

   ```powershell
   py -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```

4. Install the project packages and prepare the database:

   ```powershell
   python -m pip install -r requirements.txt
   python manage.py migrate
   ```

5. Start the site:

   ```powershell
   python manage.py runserver
   ```

6. Open http://127.0.0.1:8000/ in a browser. Stop the server with `Ctrl+C`.

If PowerShell blocks environment activation, run `python -m pip install -r requirements.txt`
without activating `.venv`, or use Command Prompt and activate with
`.venv\Scripts\activate.bat`.

## Share this project

Zip the project folder and send it. Include `manage.py`, `requirements.txt`, and the
`book`, `books`, and `static` folders. Do not include `.venv` or `__pycache__` folders;
the recipient recreates the environment using the steps above.

The current SQLite database is `db.sqlite3`. Include that file in the zip if the
recipient should get your existing library records and accounts. If you want them to
start with an empty database, leave it out; `python manage.py migrate` creates one.
They will need to create their own admin login with `python manage.py createsuperuser`
if they need Django admin access and you did not share an existing database.

This setup is for local development. Do not deploy the included Django settings to a
public server as-is.
=======
# library-management-system
>>>>>>> origin/main
