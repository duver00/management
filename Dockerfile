FROM python:3.9-alpine

# Install system dependencies for Postgres and Redis
RUN apk update && apk add --no-cache postgresql-dev gcc python3-dev musl-dev libffi-dev openssl-dev redis

# Set the working directory to /app
WORKDIR /app

# Clone the Django project from GitHub
RUN git clone https://github.com/duver00/management.git

# Install any needed packages specified in requirements.txt
RUN pip install --update pip
RUN pip install-r repo/requirements.txt

# copy project
COPY . .