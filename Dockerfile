FROM python:3.8

WORKDIR /inventory_service

COPY requirements.txt /inventory_service/
RUN pip install --no-cache-dir -r requirements.txt

COPY . /inventory_service/

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
