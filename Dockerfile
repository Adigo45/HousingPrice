
# official python image
From python:3.9-slim-buster


# Set the working directory in the conatiner
WORKDIR /app

# Install dependencies
COPY . .

RUN pip install -r requirements.txt

## Expose port 8000
EXPOSE 8000

#Run app.py when the container launches

CMD ["gunicorn", "-w", "4", "app:app", "-b", "0.0.0.0:8000"]

