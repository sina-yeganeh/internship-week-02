import logging
from logging.handlers import RotatingFileHandler
from flask import Flask, request

import os
import json

class JSONFormater(logging.Formatter):
  def format(self, record):
    log = {
      "time": self.formatTime(record, self.datefmt),
      "level": record.levelname,
      "message": record.msg,
    }

    return json.dumps(log)

def setup_logger(app: Flask):
  if not os.path.exists("logs"):
    os.mkdir("logs")

  handler = RotatingFileHandler(
    filename="logs/app.log",
    maxBytes=1000000,
    backupCount=10
  )

  handler.setLevel(logging.INFO)
  handler.setFormatter(JSONFormater())

  app.logger.addHandler(handler)
  app.logger.setLevel(logging.INFO)
  app.logger.propagate = False

  @app.before_request
  def log_request():
    log_data = {
      "ip": request.headers.get("X-Forwarded-For", request.remote_addr),
      "method": request.method,
      "path": request.path,
      "user_agent": request.headers.get("User-Agent")
    }
    app.logger.info(log_data)

  @app.after_request
  def log_respones(response):
    log_data = {
      "ip": request.headers.get("X-Forwarded-For", request.remote_addr),
      "method": request.method,
      "path": request.path,
      "status_code": response.status_code,
      "user_agent": request.headers.get("User-Agent")
    }
    app.logger.info(log_data)
    return response 