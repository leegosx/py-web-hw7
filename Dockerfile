FROM python:3.11.4

# Set an environment variable
ENV APP_HOME /app

ENV DEBIAN_FRONTEND=noninteractive

# Set the working directory inside the container
WORKDIR $APP_HOME

# Copy the other files to the working directory of the container
COPY pyproject.toml $APP_HOME/pyproject.toml
COPY poetry.lock $APP_HOME/poetry.lock

# Install dependencies inside the container
RUN pip install poetry

COPY . .

# Specify the port on which the application runs inside the container
EXPOSE 5000

# Run our application inside the container
ENTRYPOINT ["python", "src/main.py"]