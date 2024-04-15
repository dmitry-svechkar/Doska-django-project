FROM python:3.9

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt && pip install --upgrade pip 

COPY . /app
EXPOSE 8000
# CMD ["python", "manage.py", "runserver"]
# CMD ["gunicorn", "--bind", "0.0.0.0:8000", "table.wsgi"]