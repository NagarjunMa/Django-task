#   Django REST API for Item Dashboard
This Django project provides a RESTful API for an item dashboard, including features like data models definition, database connection, API endpoints, serialization, query parameters, documentation, authentication, and testing. Additionally, it includes caching for optimized performance and a basic front-end interface.

##  Features
-   Data Models: Custom Django data models to represent items, categories, and tags.
-   Database Connection: Configuration options for both SQL and NoSQL databases.
-   API Endpoints: A comprehensive set of endpoints for accessing item data.
-   Serialization: Utilizes Django REST Framework for efficient serialization.
-   Query Parameters: Supports advanced filtering through query parameters.
-   API Documentation: Detailed API documentation including request and response examples.
-   Authentication: Secure access through token-based authentication.
-   Testing: Includes unit tests for all API endpoints.
-   Caching: Implements caching to improve API response times.
-   Front-end Interface: A basic front-end consuming the API and presenting data.
### Getting Started
    Prerequisites
        Python 3.8+
        Django 3.2+
        Django REST Framework
    Database System - MySQL


### Installation & Running Locally
1. Clone this repository into your local machine using `git clone https://github.com/NagarjunMa/Django-task
2. Clone the repository:
    `git clone git@github.com:NagarjunMa/Django-task.git`
3. Install required Python packages:
    `pip install -r requirements.txt`
4. Set up a new virtual environment (optional but recommended):
   1.  Create venv directory: `mkdir django_venv && cd django_venv`
5. Configure your database in settings.py:
    - Install the mysqlclient using following commands
        `$ brew install mysql pkg-config`
        `$ pip install mysqlclient`
6. Migrate the database:
        `python manage.py migrate`
7. Create a superuser:
        `python manage.py createsuperuser`
### Running the Application

Start the Django development server:
    `python manage.py runserver`
Access the API Documentation - https://django-task-nm-cda857f8d0ee.herokuapp.com/swagger/
Access the  application using the link - https://django-task-nm-cda857f8d0ee.herokuapp.com/login/


### Testing
    `python manage.py test`

#### Documentation

Caching: Enabled on item listing endpoints to reduce load times.
Front-end Interface: Accessible at the root URL, displaying items in a user-friendly format.

### Deployment
Refer to the deployment guide for your chosen cloud provider (Heroku, AWS, Azure) for instructions on deploying this Django application.