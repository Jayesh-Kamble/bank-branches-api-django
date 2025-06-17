# 🏦 Bank Branches API – Built with Django REST Framework

A lightweight and performant REST API for managing Indian bank and branch data. This project demonstrates advanced search, filtering, pagination, and admin tools using Django and DRF.

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Django](https://img.shields.io/badge/Django-5.2.3-green.svg)
![DRF](https://img.shields.io/badge/DRF-3.14.0-red.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

---

## 🔍 About the Project

This project was developed to showcase a well-structured Django REST API that supports:
- Efficient search/filtering of bank branches
- Clean admin interface for managing records
- Optimized queries with proper DB relationships

It’s ideal for anyone looking for a reliable backend for financial apps or learning DRF.

---

## 🚀 Features

- 📚 RESTful APIs with pagination & search
- 🏢 Admin panel for banks & branches
- 🧠 Search by IFSC, city, state, or bank
- 🔐 Input validation & error handling
- ⚡ Optimized using `select_related`
- 🌍 CORS enabled for frontend integration

---

## 📸 Screenshots

**Landing Page**
![Landing](https://github.com/user-attachments/assets/ff982c7e-b860-4deb-9bb8-66f3621ea591)

**Features View**
![Features](https://github.com/user-attachments/assets/481b8498-1463-4f31-8a49-2005605cf7ff)

---

## 📁 Tech Stack

- **Backend:** Django 5.2.3 + DRF 3.14.0  
- **DB:** SQLite (dev), PostgreSQL ready  
- **Tools:** VS Code, GitHub, Django Admin  
- **Libs:** `django-filter`, `django-cors-headers`, `python-decouple`

---

## 🌐 API Overview

### Endpoints
| Method | Endpoint | Purpose |
|--------|----------|---------|
| GET | `/api/banks/` | List all banks |
| GET | `/api/banks/{id}/` | Bank detail |
| GET | `/api/banks/{id}/branches/` | All branches for a bank |
| GET | `/api/branches/` | List all branches (with filters) |
| GET | `/api/branches/{id}/` | Branch detail |

### Filters
- `search`: Across IFSC, branch, city, state
- `city`, `state`, `bank`: Exact matches
- `ordering`: e.g. `?ordering=branch`, `-created_at`

---

## ⚙️ Getting Started

```bash
git clone https://github.com/Jayesh-Kamble/bank-branches-api-django.git
cd bank-branches-api-django
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
