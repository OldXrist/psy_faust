# Psychologist Personal Website

This is a personal website project for a psychologist, built with Django. The website includes features such as an about section, personal statistics, qualifications section, service listings, and a contact section. The website aims to provide an easy-to-navigate online presence for the psychologist and a way to connect with clients.

---

## Features

- **About**: Introduces the psychologist and their philosophy.
- **Statistics**: Provides personal statistics about psychologists work
- **Qualifications**: Presents professional qualifications such as diplomas, certificates etc.
- **Services**: Detailed descriptions of offered psychological services.
- **Contacts**: Clients can get in touch directly from the website.
- **Responsive Design**: Optimized for both desktop and mobile devices.

---

## Prerequisites

Before starting, ensure you have the following installed on your system:

- Python 3.9+
- pip (Python package installer)
- Git
- SQLite (pre-installed with Python)
- Virtualenv

---

## Installation Guide

1. **Clone the Repository**  
   ```bash
   git clone https://github.com/OldXrist/psy_faust.git
   cd psy_faust
   ```

2. **Create and Activate a Virtual Environment**  
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**  
   ```bash
   pip install poetry
   poetry install
   ```

4. **Set Up the Database**  
   Apply the migrations to set up the SQLite database:  
   ```bash
   python manage.py migrate
   ```

5. **Collect Static Files**  
   Gather all static files into the `staticfiles` directory:  
   ```bash
   python manage.py collectstatic
   ```

6. **Run the Development Server**  
   Start the development server:  
   ```bash
   python manage.py runserver
   ```
   Open your browser and visit [http://127.0.0.1:8000](http://127.0.0.1:8000) to view the site.

---
## Deployment

To deploy this project on a live server:

1. Use a **Linux-based VPS (e.g., Ubuntu)**.
2. Configure **Gunicorn** and **Nginx** to serve the application.
3. Set up the project in **production mode** (update `settings.py`).
4. Ensure **media** and **static files** are properly served.

See the [Deployment Guide](#) for detailed instructions.