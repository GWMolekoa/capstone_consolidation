# Django Capstone Project

## Setup

### Virtual Environment

1. Create and activate a virtual environment:
   
   python -m venv env
   source env/bin/activate  # Unix/macOS
   .\env\Scripts\activate   # Windows

2. Install the required packages:

    pip install --no-cache-dir -r requirements.txt


### Django Development Server

3. Run the development server:

    python manage.py runserver


### Docker

1. Build the Docker image:

    docker build -t gwmolekoa/capstone:latest .

2. Run the Docker container:

    docker run -p 8000:8000 gwmolekoa/capstone:latest


### Documentation

The documentation is generated using Sphinx and can be found in the 'docs/_build/html/' directory. The documentation can be viewed by opening 'index.html'.
