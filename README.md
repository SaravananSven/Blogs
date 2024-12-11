# Blogs
This is a Django-based blog API project, built using Django REST Framework. The API allows users to create and manage blog posts. It uses token-based authentication to secure endpoints, ensuring only authorized users can create, retrieve, update, or delete blog posts.

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Run Locally Instructions</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            margin: 20px;
        }
        pre {
            background-color: #f4f4f4;
            border: 1px solid #ddd;
            padding: 10px;
            overflow-x: auto;
        }
        code {
            font-family: "Courier New", Courier, monospace;
            background-color: #f9f9f9;
            padding: 2px 4px;
        }
        a {
            color: #007bff;
            text-decoration: none;
        }
        a:hover {
            text-decoration: underline;
        }
        h1, h2 {
            color: #333;
        }
    </style>
</head>
<body>
    <h1>Run Locally</h1>
    <p>Follow these steps to set up and run the <strong>Blogs</strong> Django API project locally:</p>
    
    <h2>1. Clone the repository</h2>
    <pre><code>git clone https://github.com/SaravananSven/Blogs.git
cd Blogs
    </code></pre>
    
    <h2>2. Set up a virtual environment</h2>
    <p>Create and activate a virtual environment:</p>
    <p><strong>For Linux/macOS:</strong></p>
    <pre><code>python3 -m venv env
source env/bin/activate
    </code></pre>
    <p><strong>For Windows:</strong></p>
    <pre><code>python -m venv env
.\env\Scripts\activate
    </code></pre>
    
    <h2>3. Install dependencies</h2>
    <p>Install the required Python packages using <code>pip</code>:</p>
    <pre><code>pip install -r requirements.txt</code></pre>
    
    <h2>4. Configure environment variables</h2>
    <p>Create a <code>.env</code> file in the root directory and add the following variables:</p>
    <pre><code>SECRET_KEY=your-django-secret-key
DEBUG=True
ALLOWED_HOSTS=127.0.0.1,localhost
    </code></pre>
    <p>Replace <code>your-django-secret-key</code> with a valid Django secret key.</p>
    
    <h2>5. Set up the database</h2>
    <p>Apply migrations to initialize the database schema:</p>
    <pre><code>python manage.py makemigrations
python manage.py migrate
    </code></pre>
    
    <h2>6. Create a superuser (optional)</h2>
    <p>If you need admin access, create a superuser account:</p>
    <pre><code>python manage.py createsuperuser</code></pre>
    <p>Follow the prompts to set up the admin credentials.</p>
    
    <h2>7. Generate API tokens</h2>
    <p>To access authenticated endpoints, generate an API token for a user:</p>
    <pre><code>python manage.py drf_create_token &lt;username&gt;</code></pre>
    <p>Replace <code>&lt;username&gt;</code> with an existing username or the superuser account.</p>
    
    <h2>8. Start the development server</h2>
    <p>Run the development server:</p>
    <pre><code>python manage.py runserver</code></pre>
    <p>Access the API at <a href="http://127.0.0.1:8000/api/" target="_blank">http://127.0.0.1:8000/api/</a>.</p>
    
    <h2>9. Test the API</h2>
    <p>Use <a href="https://www.postman.com/" target="_blank">Postman</a> or <a href="https://curl.se/" target="_blank">curl</a> to test the API endpoints.</p>
    <p>For authenticated requests, include the token in the <code>Authorization</code> header:</p>
    <pre><code>Authorization: Token &lt;your-token&gt;</code></pre>
</body>
</html>

