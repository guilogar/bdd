import math

from src.exceptions.negativeRadius import NegativeRadius

def radiusArea(radius = 0.1):
  if (radius <= 0):
    raise NegativeRadius()
  else:
    return radius * radius * math.pi