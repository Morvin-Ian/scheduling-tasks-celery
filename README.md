# Django Celery Integration

This repository demonstrates the integration of Celery with a Django project for asynchronous task execution.

## Requirements

- Python 
- Django 
- Celery 
- Redis (as message broker)
- (Optional) Supervisord or systemd for managing Celery workers in production

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/Morvin-Ian//django-celery.git
    ```

2. Create a virtual environment and activate it:

    ```bash
    cd django-celery
    python -m venv venv
    source venv/bin/activate  # For Unix or MacOS
    # Or
    venv\Scripts\activate  # For Windows
    ```

3. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Set up Celery configuration:

    - Update `settings.py` with Celery settings.
    - Configure a message broker (RabbitMQ or Redis) in the settings.
    - Define Celery tasks in your Django app.

5. Start Celery worker:

    ```bash
    celery -A app worker -l info
    ```

6. Run Django server:

    ```bash
    python manage.py runserver
    ```

7. Visit `http://127.0.0.1:8000/` in your browser to access the Django application.

## Usage

- Define Celery tasks using the `@task` decorator.
- Use `delay()` method to enqueue tasks for asynchronous execution.

Example:

```python
from celery import shared_task

@shared_task
def send_email_task(email):
    # Your task logic here
    pass
