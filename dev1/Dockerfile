FROM python:3.11
WORKDIR /app
ENV PYTHONUNBUFFERED=1

COPY . .
CMD [ "python3", "./scripts/ssh_agent_forwarding.py" ]