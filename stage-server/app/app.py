from flask import Blueprint, request, jsonify

from .modules.weather import get_weather
from .modules.quote_gen import create_quote

main_bp = Blueprint("main", __name__)

@main_bp.route("/my-ip")
def my_ip_route():
  return {
    "ip": request.headers.get("X-Forward-For", request.remote_addr)
  }

@main_bp.route("/weather", methods=["POST"])
def weather_route():
  data = request.get_json(force=True)
  return jsonify(get_weather(data["api-key"], data["place"]))

@main_bp.route("/quote")
def quate_route():
  return {
    "quote": create_quote()
  }