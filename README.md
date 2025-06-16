# Bank Branches REST API 🏦

A comprehensive Django REST API for managing bank and branch information across India. This project provides robust endpoints for searching, filtering, and retrieving bank branch details with advanced query capabilities.

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://python.org)
[![Django](https://img.shields.io/badge/Django-5.2.3-green.svg)](https://djangoproject.com)
[![Django REST Framework](https://img.shields.io/badge/DRF-3.14.0-red.svg)](https://django-rest-framework.org)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

## 📋 Table of Contents

- [Features](#features)
- [Technology Stack](#technology-stack)
- [API Endpoints](#api-endpoints)
- [Installation & Setup](#installation--setup)
- [Usage Examples](#usage-examples)
- [Screenshots](#screenshots)
- [Database Schema](#database-schema)
- [Project Structure](#project-structure)
- [Performance](#performance)
- [Contributing](#contributing)
- [Contact](#contact)

## ✨ Features

- **Complete REST API** with full CRUD operations
- **Advanced Search & Filtering** by bank name, city, state, IFSC code
- **Pagination Support** for efficient data loading (20 items per page)
- **Admin Interface** for easy data management
- **CORS Enabled** for frontend integration
- **Comprehensive Error Handling** with proper HTTP status codes
- **Database Optimization** with select_related for better performance
- **Professional Logging** system for monitoring and debugging
- **Browsable API** interface for easy testing and documentation
- **Input Validation** and data integrity checks
- **Unique IFSC Code** enforcement across all branches

## 🛠️ Technology Stack

**Backend Framework:**
- Django 5.2.3
- Django REST Framework 3.14.0

**Database:**
- SQLite (Development)
- PostgreSQL Ready (Production)

**Additional Libraries:**
- django-cors-headers (CORS support)
- django-filter (Advanced filtering)
- python-decouple (Environment management)

**Development Tools:**
- Git & GitHub (Version Control)
- VS Code (IDE)
- Postman (API Testing)

## 🚀 API Endpoints

### Banks Endpoints

| Method | Endpoint | Description | Parameters |
|--------|----------|-------------|------------|
| GET | `/api/banks/` | List all banks | `search`, `ordering` |
| GET | `/api/banks/{id}/` | Get specific bank | - |
| GET | `/api/banks/{id}/branches/` | Get bank's branches | - |

### Branches Endpoints

| Method | Endpoint | Description | Parameters |
|--------|----------|-------------|------------|
| GET | `/api/branches/` | List all branches | `search`, `city`, `state`, `bank`, `ordering` |
| GET | `/api/branches/{id}/` | Get specific branch | - |

### Query Parameters

- **search**: Search across bank names, branch names, IFSC codes, cities
- **city**: Filter by city name (exact match)
- **state**: Filter by state name (exact match)
- **bank**: Filter by bank ID
- **ordering**: Sort by field (prefix with `-` for descending)
  - Available fields: `branch`, `created_at`, `bank__name`

### Example API Calls

#### Get All Banks

**API Call:**
**Screenshot:**
![Banks API Response](screenshots/banks-api-response.png)

