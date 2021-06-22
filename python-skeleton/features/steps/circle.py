from behave import *
from src.circleArea import radiusArea
from src.exceptions.invalidRadius import InvalidRadius

globalRadius = 0

@given('un radio de {radius} m')
def step_impl(context, radius):
    radius = float(radius)
    global globalRadius
    globalRadius = radius

    assert True

@when('al calcular el area')
def step_impl(context):
    assert True

@when('al calcular el area, se lanza una exception de tipo InvalidRadius')
def step_impl(context):
    try:
        radiusArea(globalRadius)
        assert False
    except InvalidRadius:
        assert True
    except Exception:
        assert False
    
@then('devuelve un valor aproximado a {result} m con un error absoluto de {error}')
def step_impl(context, result, error):
    result = float(result)
    error = float(error)

    area = radiusArea(globalRadius)
    absoluteError = abs(area - result)

    assert (absoluteError < error)