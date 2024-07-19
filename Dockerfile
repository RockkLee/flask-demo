FROM python:3.11.0

# RUN apt-get update && apt-get install -y tree

# cd to the dir, and if the dir does not exist, create it
WORKDIR /flask-demo/

# Copy the necessary files and directories
COPY app.py ./
COPY flask_demo ./flask_demo
COPY tests ./tests

# Copy the requirements.txt file
COPY requirements.txt ./
# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port the app runs on
#EXPOSE 8000

CMD ["gunicorn", "-c", "./flask_demo/config/gunicorn_config.py", "app:app"]