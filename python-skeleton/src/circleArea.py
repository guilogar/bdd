import math
from src.exceptions.invalidRadius import InvalidRadius

def radiusArea(radius = 0.1):
  if radius <= 0:
    raise InvalidRadius
  else:
    return radius * radius * math.pi