# Titanic Survival Prediction - Django Web App 🛳️

A web application that predicts survival on the Titanic using a pre-trained ML model, built with Django and deployed with Gunicorn and Nginx.  

![Python](https://img.shields.io/badge/Python-3.12-blue) ![Django](https://img.shields.io/badge/Django-5.2.6-green) ![AWS](https://img.shields.io/badge/AWS-EC2-orange)

---

## Overview

This is a **full-stack Django project** that allows users to input passenger data and get a prediction of survival. It demonstrates the integration of **machine learning** with a web application and basic deployment skills.

---

## Features ✨

- User-friendly form to input passenger details  
- Machine Learning model predicts survival probability  
- Display results on a separate page  
- Responsive design with templates  

---

## Screenshots 📸
1. **Index Page**  
![Index Page](https://github.com/user-attachments/assets/62dabba0-7762-4a96-a9c1-1d2afaf74050)

2. **Result Page**  
![Result Page](https://github.com/user-attachments/assets/1d684e05-d7e5-42e5-9f7f-af6e9d669ba1)

3. **Terminal / Deployment Logs**  
![Terminal](https://github.com/user-attachments/assets/d9572c46-b62d-4ba7-bdf1-93118c9bd18c)
---

## Installation & Setup 🛠️

1. **Clone the repository**  
```bash
git clone https://github.com/yourusername/titanic-django.git
cd titanic-django/backend
```

2. **Create and activate virtual environment**
```bash
python3 -m venv venv
source venv/bin/activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Apply migrations**
```bash
python manage.py migrate
```

5. **Run server locally**
```bash
python manage.py runserver
```
> Open `http://127.0.0.1:8000/` in your browser.

---

## Deployment 🚀

This project was deployed on an **AWS EC2 instance** using Gunicorn and Nginx:

1. **Gunicorn Service**

   * Configured as a `systemd` service
   * Runs the Django app in the background

2. **Nginx Reverse Proxy**

   * Forwards HTTP requests to Gunicorn
   * Configured with Unix socket

3. **Important Notes**

   * `ALLOWED_HOSTS` must include your server IP or domain
   * After stopping the instance, services need to be enabled with systemctl

---

## Project Structure 📂

```
backend/            # Django project
├─ templates/       # HTML templates
├─ db.sqlite3       # SQLite database
├─ manage.py        # Django management script
├─ titanic_model.sav # Pre-trained ML model
```

---

## Key Learnings 🧠

This project demonstrates **real-world deployment and backend management skills**:

* AWS EC2 provisioning and SSH access
* Django deployment with Gunicorn
* Nginx reverse proxy setup
* Systemd service creation for automatic startup
* Debugging 502 Bad Gateway and DisallowedHost issues
* Organizing project structure for backend, templates, and static files

> Even if the site is no longer live, this shows hands-on experience in **full-stack deployment**, bridging development and production.

---

## License

MIT License © \AtharvaSagane
