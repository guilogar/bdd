from behave import *
from src.circleArea import radiusArea
from src.exceptions.negativeRadius import NegativeRadius

globalRadius = 0

@given('un radio de valor {radius}')
def step_impl(context, radius):
    assert radius.replace('.', '').replace('-', '').isnumeric()
    radius = float(radius)

    global globalRadius
    globalRadius = radius

@when('al calcular el area')
def step_impl(context):
    pass

@when('al calcular el area, lanza una exception de tipo NegativeRadius')
def step_impl(context):
    try:
        global globalRadius
        radiusArea(globalRadius)
        assert False
    except NegativeRadius:
        assert True

@then('el area es igual a ~{value} con un error absoluto menor que {absoluteErrorLine}')
def step_impl(context, value, absoluteErrorLine):
    value = float(value)
    absoluteErrorLine = float(absoluteErrorLine)
    
    global globalRadius
    area = radiusArea(globalRadius)
    absoluteError = abs(area - value)
    assert absoluteError < absoluteErrorLine