FROM python:3.8

WORKDIR /inventory

COPY requirements.txt /inventory/
RUN pip install --no-cache-dir -r requirements.txt

COPY . /inventory/

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
