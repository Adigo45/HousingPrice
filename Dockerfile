
# official python image
From python:3.9-slim-buster


# Set the working directory in the conatiner
WORKDIR /app

# Install dependencies
COPY . /app

RUN pip install -r requirements.txt

EXPOSE 5000

#Run app.py when the container launches

CMD ["flask", "run", "--host=0.0.0.0"]
