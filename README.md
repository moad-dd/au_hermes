# AU HERMES - HR Management System

A comprehensive Human Resources Management System built with Django.

## Features

- Employee Management (Civil Servants & Administrative Staff)
- Leave Request Management
- Salary & Payroll Management
- Document Generation (Work Certificates, Pay Slips)
- Career History Tracking
- User Role Management

## Setup Instructions

1. Activate virtual environment:
   ```bash source venv/bin/activate```

2. Apply migrations:
   ```bash python manage.py makemigrations python manage.py migrate```

3. Create superuser:
   ```bash python manage.py createsuperuser```

4. Run server:
   ```bash python manage.py runserver```

## Default Access

- URL: <http://127.0.0.1:8000>
- Admin: <http://127.0.0.1:8000/admin>

## Database Configuration

- Database: au_hermes_db
- User: moad
- Engine: MySQL
