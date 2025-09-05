FROM python:3.11
WORKDIR /app
ENV PYTHONUNBUFFERED=1

RUN sudo apt update && sudo apt install -y openssh-client && rm -rf /var/lib/apt/lists/*

COPY . .
CMD [ "python3", "./scripts/passwordless_auth.py" ]