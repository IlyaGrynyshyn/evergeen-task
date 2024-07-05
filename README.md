# Evergeen task

## User interface

### Main page

![Screenshot from 2024-07-05 18-49-50.png](static%2Freadme-images%2FScreenshot%20from%202024-07-05%2018-49-50.png)

### Detail page

![img.png](static%2Freadme-images%2Fimg.png)

## Usage Instructions

Python must be already installed.

1. **Installation:**
    - Clone the repository to your local machine `https://github.com/IlyaGrynyshyn/evergeen-task.git`.
    - Create virtual environment `python3 -m venv venv`
    - Install the required dependencies using `pip install -r requirements.txt`.

2. **Running:**
    - Apply migrations `python manage.py migrate`
    - Start the server with `python manage.py runserver`.
    - Access the store via `http://localhost:8000` in your web browser.

## Docker

To run the Notes App project using Docker Compose:
- Start the containers: `docker-compose up --build`
- Access the application at http://localhost:8000