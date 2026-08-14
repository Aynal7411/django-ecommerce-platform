# Django E-commerce Platform

A full-stack e-commerce platform built with **Python and Django**.

This project is designed to demonstrate real-world Django development practices including custom user authentication, product and category management, shopping cart functionality, database relationships, Django templates, static/media file handling, and scalable project architecture.

---

## Project Overview

The Django E-commerce Platform is an online clothing store where customers can browse products, explore categories, create accounts, manage their profiles, add products to a shopping cart, and prepare products for checkout.

The project is being developed with a focus on clean architecture, maintainability, security, and real-world e-commerce workflows.

---

## Features

### Authentication & Account Management

- Custom User Model
- Mobile number based authentication
- User registration
- User login/logout
- Password hashing using Django's authentication system
- User profile
- Staff user support
- Superuser support
- Active/inactive user management
- Created and updated timestamps

### Product Management

- Product listing
- Product details
- Product images
- Product pricing
- Product availability
- Product categorization
- Product search/filtering
- Product management through Django Admin

### Category Management

- Product categories
- Category-based product browsing
- Category management
- Slug-based URLs

### Shopping Cart

- Add product to cart
- Remove product from cart
- Update product quantity
- Cart item management
- Cart total calculation
- User-specific cart

### Admin Management

Django Admin can be used to manage:

- Users
- Products
- Categories
- Cart items
- Product images
- Store data

---

## Technology Stack

### Backend

- Python
- Django
- Django ORM
- Django Authentication System

### Database

- SQLite for development
- PostgreSQL recommended for production

### Frontend

- HTML5
- CSS3
- JavaScript
- Django Templates
- Bootstrap / Custom CSS

### Development Tools

- Git
- GitHub
- VS Code
- Python Virtual Environment

---

## Project Architecture

```text
django-ecommerce-platform/
│
├── account/
│   ├── migrations/
│   ├── models.py
│   ├── forms.py
│   ├── views.py
│   ├── api_views.py
│   ├── urls.py
│   └── admin.py
│
├── product/
│   ├── migrations/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── admin.py
│
├── category/
│   ├── migrations/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── admin.py
│
├── cart/
│   ├── migrations/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── admin.py
│
├── cloth_business/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── templates/
│
├── static/
│
├── media/
│
├── manage.py
├── requirements.txt
├── .gitignore
└── README.md


#installation
git clone https://github.com/Aynal7411/django-ecommerce-platform.git
cd django-ecommerce-platform
