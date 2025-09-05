import pyquotegen

def create_quote(cat: str = "motivational"):
  return pyquotegen.get_quote(cat)
