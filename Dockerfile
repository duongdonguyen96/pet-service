# Dockerfile

# Stage 1: Build stage
FROM python:3.12-slim AS builder

# set work directory
WORKDIR /app

# set env variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
COPY requirements.txt /app/
RUN pip install --user -r /app/requirements.txt

# Stage 2: Final stage
FROM python:3.12-slim

# set work directory
WORKDIR /app

# set env variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# copy only the necessary files from the build stage
COPY --from=builder /root/.local /root/.local
ENV PATH=/root/.local/bin:$PATH

# copy project
COPY ./app /app/app

EXPOSE 8001

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8001", "--reload"]