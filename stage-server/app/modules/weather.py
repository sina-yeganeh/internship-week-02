from pyowm import OWM

def get_weather(api_key: str, place: str):
  owm = OWM(api_key)
  mgr = owm.weather_manager()

  w = mgr.weather_at_place(place).weather
  result = {
    "status": w.detailed_status,
    "temperature": w.temperature('celsius'),
    "humidity": w.humidity
  }

  return result