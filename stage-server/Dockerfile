FROM python:3.11
WORKDIR /app
ENV PYTHONBUFFERD=1

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .
CMD [ "python3", "run.py" ]
