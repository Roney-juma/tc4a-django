# TC4A-django Application Documentation
## Overview
This Django application provides a basic customer and order management system. It includes a REST API for CRUD operations on customers and orders, with authentication and authorization handled via OpenID Connect. It also integrates with Africa's Talking SMS gateway to send notifications.

Deployed URL:` https://tc4a-django.onrender.com`
Features
Customer Management:

### Endpoints:
GET /api/customers/ - List all customers
POST /api/customers/ - Create a new customer
GET /api/customers/{id}/ - Retrieve a specific customer
PUT /api/customers/{id}/ - Update a specific customer
DELETE /api/customers/{id}/ - Delete a specific customer


### Order Management:

Endpoints:
GET /api/orders/ - List all orders
POST /api/orders/ - Create a new order
GET /api/orders/{id}/ - Retrieve a specific order
PUT /api/orders/{id}/ - Update a specific order
DELETE /api/orders/{id}/ - Delete a specific order


### Authentication and Authorization:

Uses OpenID Connect for secure user authentication.
Login Endpoint:
/api/token/ - Obtain JWT token

Protected Endpoints:
All customer and order endpoints require authentication.
SMS Notifications:

* Sends SMS notifications to customers when a new order is created.

Installation and Setup
1. Clone the Repository

git clone `https://github.com/Roney-juma/tc4a-django`
2. Create a Virtual Environment

python3 -m venv mytest
source env/bin/activate

3. Install Dependencies
pip install -r requirements.txt
5. Apply Migrations
python manage.py migrate
6. Collect Static Files

python manage.py collectstatic --noinput
7. Run the Development Server

* python manage.py runserver

### Deployment
The application is deployed on Render. 
* https://tc4a-django.onrender.com/

