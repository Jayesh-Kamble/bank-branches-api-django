# Bank Branches REST API 🏦

A comprehensive Django REST API for managing bank and branch information across India. This project provides robust endpoints for searching, filtering, and retrieving bank branch details with advanced query capabilities.

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://python.org)
[![Django](https://img.shields.io/badge/Django-5.2.3-green.svg)](https://djangoproject.com)
[![Django REST Framework](https://img.shields.io/badge/DRF-3.14.0-red.svg)](https://django-rest-framework.org)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

## 📋 Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Technology Stack](#technology-stack)
- [API Endpoints](#api-endpoints)
- [Live Demo Screenshots](#live-demo-screenshots)
- [Installation & Setup](#installation--setup)
- [Usage Examples](#usage-examples)
- [Database Schema](#database-schema)
- [Project Structure](#project-structure)
- [Admin Interface](#admin-interface)
- [Performance](#performance)
- [Contributing](#contributing)
- [Contact](#contact)

## 🎯 Project Overview

This Django REST API project demonstrates a complete backend solution for managing Indian bank branches with advanced filtering, search capabilities, and a professional admin interface. The project showcases modern web development practices with Django REST Framework.

![Project Structure](https://github.com/user-attachments/assets/d5ad7ebf-815b-4175-92f7-45f89eb7fcac)
*Well-organized Django project structure with modular app design*

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

## 📸 Live Demo Screenshots

### Banks API Response
![Banks API](https://github.com/user-attachments/assets/e9fc5d32-e956-4b02-8807-9901921bcc26)
*Banks List API endpoint showing paginated results with comprehensive bank information including unique codes and timestamps*

### Branches API with Advanced Filtering
![Branches API](https://github.com/user-attachments/assets/13d6d543-0e91-4489-ba1a-1018f8c47cfd)
*Branches List API demonstrating rich branch data with bank relationships, IFSC codes, and location details*

### Search Functionality in Action
![Search Results](https://github.com/user-attachments/assets/21b026fd-c798-4694-86e6-c1f5fb8db7fa)
*Real-time search functionality showing filtered results based on search queries across multiple fields*

### Bank-Specific Branches Endpoint
![Bank Branches](https://github.com/user-attachments/assets/31e09f7b-9b69-4958-b914-67d7f7a33f6c)
*Dedicated endpoint showing all branches for a specific bank with detailed branch information and parent bank data*

## 📦 Installation & Setup

### Prerequisites

- Python 3.8 or higher
- Git
- Virtual Environment (recommended)

### Step-by-Step Installation

1. **Clone the Repository**
