# Blogs
This is a Django-based blog API project, built using Django REST Framework. The API allows users to create and manage blog posts. It uses token-based authentication to secure endpoints, ensuring only authorized users can create, retrieve, update, or delete blog posts.
## Table of Contents
- [Run Locally](#run-locally)
- [Clone the repository](#1-clone-the-repository)
- [Set up a virtual environment](#2-set-up-a-virtual-environment)



## Run Locally

Follow these steps to set up and run the **Blogs** Django API project locally:

### 1. Clone the repository

Clone this repository to your local machine:

git clone https://github.com/SaravananSven/Blogs.git
cd Blogs

### 2. Set up a virtual environment

For Windows:


```bash
python -m venv env
.\env\Scripts\activate

### 3. Install dependencies

Install the required Python packages using pip:

bash
Copy code
pip install -r requirements.txt

### 4. Configure environment variables
Create a .env file in the root directory and add the following variables:

bash
Copy code
SECRET_KEY=your-django-secret-key
DEBUG=True
ALLOWED_HOSTS=127.0.0.1,localhost
Replace your-django-secret-key with a valid Django secret key.


###5. Set up the database
Apply migrations to initialize the database schema:

bash
Copy code
python manage.py makemigrations
python manage.py migrate

###6. Create a superuser (optional)
If you need admin access, create a superuser account:

bash
Copy code
python manage.py createsuperuser
Follow the prompts to set up the admin credentials.

###7. Generate API tokens
To access authenticated endpoints, generate an API token for a user:

bash
Copy code
python manage.py drf_create_token <username>
Replace <username> with an existing username or the superuser account.

###8. Start the development server
Run the development server:

bash
Copy code
python manage.py runserver
Access the API at http://127.0.0.1:8000/api/.

###9. Test the API
Use Postman or curl to test the API endpoints. For authenticated requests, include the token in the Authorization header:

bash
Copy code
Authorization: Token <your-token>



