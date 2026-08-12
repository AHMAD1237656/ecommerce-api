# 🛒 E-Commerce REST API

A complete and scalable **E-Commerce REST API** built with **Django REST Framework** and **PostgreSQL**.

This project was developed as **Task 3 of the InternGrow Internship Programs**, focusing on building a structured backend system with product management, shopping cart, orders, wishlist, reviews, coupons, inventory management, and payment functionality.

---

## 🚀 Features

### 📦 Product Management
- Product CRUD operations
- Category management
- Product image upload
- Product search
- Product filtering
- Pagination

### 👤 Customer Management
- Customer CRUD operations
- Customer information management

### 🛒 Shopping Cart
- Create and manage shopping carts
- Add products to cart
- Update product quantities
- Remove products from cart

### 📋 Order Management
- Create and manage orders
- Order items management
- Order status tracking
- Shipping address management
- Order tracking API

### ❤️ Wishlist
- Add products to wishlist
- Remove products from wishlist
- View wishlist items

### ⭐ Reviews
- Product reviews
- Product ratings
- Review management

### 🎟️ Coupons
- Coupon creation and management
- Discount handling
- Coupon validation

### 📊 Inventory
- Product stock management
- Inventory tracking
- Stock availability management

### 💳 Payment
- Stripe Payment Gateway integration
- Payment Intent creation
- Payment status handling

### 🧾 Invoice
- PDF invoice generation
- Order invoice download

### 📧 Email Notifications
- Order confirmation email notifications

---

## 🛠️ Technologies Used

- **Python**
- **Django 6.1**
- **Django REST Framework**
- **PostgreSQL**
- **Django Filters**
- **DRF Spectacular**
- **Simple JWT**
- **Stripe**
- **ReportLab**
- **python-dotenv**

---

## 📁 Project Structure

```text
Ecommerce_API/
│
├── config/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── products/
├── categories/
├── customers/
├── cart/
├── orders/
├── wishlist/
├── reviews/
├── coupons/
├── inventory/
│
├── manage.py
├── .gitignore
└── README.md
