# Pet-Service

## Getting Up and Running Locally With Docker

### Prerequisites:
- Docker; if you don’t have it yet, follow the [installation instructions](https://docs.docker.com/install/#supported-platforms)
- Docker Compose; refer to the official documentation for the [installation guide](https://docs.docker.com/compose/install/)

### Build the Stack
    $ cp env.example.yaml .env
    $ docker-compose build

### Run the Stack

    $ docker-compose up -d

### Build and Run the Stack

    $ pip3 install uv
    $ uv venv -p python3.12
    $ source .venv/bin/activate
    $ uv pip install -r requirements.txt

### Migration
    $ docker ps
    $ docker exec -it <container_id_of_chatbot_web> sh
    
    # Mark the current database as the latest version   
    $ alembic stamp head

    # Create a new migration
    $ alembic revision --autogenerate -m "migration message"
    
    # Apply the migration
    $ alembic upgrade head
[Alembic document](https://alembic.sqlalchemy.org/en/latest/tutorial.html)

### Access the Application
http://localhost:8000/#/


