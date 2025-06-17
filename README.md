# 🏦 Bank Branches REST API

A Django REST API for managing bank and branch information across India with advanced search, filtering, and admin support.

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://python.org)
[![Django](https://img.shields.io/badge/Django-5.2.3-green.svg)](https://djangoproject.com)
[![DRF](https://img.shields.io/badge/DRF-3.14.0-red.svg)](https://www.django-rest-framework.org/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

---

## 📋 Table of Contents

- [Overview](#overview)
- [Key Features](#key-features)
- [API Endpoints](#api-endpoints)
- [Live Demo](#live-demo)
- [Admin Interface](#admin-interface)
- [Installation](#installation)
- [Testing](#testing)
- [Tech Stack](#tech-stack)
- [Project Metrics](#project-metrics)
- [What This Demonstrates](#what-this-demonstrates)
- [Contact](#contact)

---

## 🎯 Overview

This project offers a fully functional backend system to manage Indian bank branches. Built using Django and Django REST Framework, it features advanced search, optimized queries, and a professional admin interface.

### ✅ What I Built

- 5 REST API endpoints for banks and branches
- Advanced filtering by city, state, IFSC, and bank name
- Admin panel for CRUD operations
- 17 test cases with 100% success rate
- Responsive landing & feature pages for demonstration

---

## ✨ Key Features

- **RESTful API Design** with clean, scalable endpoints
- **Advanced Search & Filtering** using query params
- **Pagination Support** (20 items per page)
- **Admin Dashboard** for secure data management
- **Optimized Queries** with `select_related`
- **Full Test Suite** for model & API validation
- **Error Handling** with clear HTTP status codes

---

## 🚀 API Endpoints

| Method | Endpoint                        | Description                        |
|--------|---------------------------------|------------------------------------|
| GET    | `/api/banks/`                  | List all banks                     |
| GET    | `/api/banks/{id}/`             | Get specific bank details          |
| GET    | `/api/branches/`               | List branches with filters         |
| GET    | `/api/branches/{id}/`          | Get specific branch details        |
| GET    | `/api/banks/{id}/branches/`    | List all branches for one bank     |

**Query Parameters:**
- `search`: Across name, IFSC, city, state
- `city`, `state`, `bank`: Exact filters
- `ordering`: Sort by field (`-created_at`, `branch`, etc.)

---

## 📸 Live Demo

**Landing Page**
![Landing Page](https://github.com/user-attachments/assets/ff982c7e-b860-4deb-9bb8-66f3621ea591)

**Features Overview**
![Features](https://github.com/user-attachments/assets/481b8498-1463-4f31-8a49-2005605cf7ff)

**Banks API**
![Banks API](https://github.com/user-attachments/assets/25741c7e-ff7c-4dd0-8d0c-f08396461ca5)

**Branches with Filters**
![Branches API](https://github.com/user-attachments/assets/66f0e475-c966-4786-8799-e31320fd7b55)

**Filtered Response**
![Filtered](https://github.com/user-attachments/assets/6eddd25a-fbbf-442d-bef9-c345af962b86)

---

## 🔧 Admin Interface

**Dashboard**
![Admin](https://github.com/user-attachments/assets/823632b1-d485-41ba-a125-f09033add3b8)

**Bank Management**
![Bank Management](https://github.com/user-attachments/assets/b7f37abf-423e-461a-b396-a932071b0feb)

**Branch Management**
![Branch Management](https://github.com/user-attachments/assets/dfb46118-4209-40bb-8280-8fb95e1d7fb6)

---

## 📦 Installation

```bash
git clone https://github.com/Jayesh-Kamble/bank-branches-api-django.git
cd bank-branches-api-django

python -m venv venv
venv\Scripts\activate   # On Windows
# or
source venv/bin/activate  # On macOS/Linux

pip install -r requirements.txt

