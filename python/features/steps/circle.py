from behave import *
from src.circleArea import radiusArea

globalRadius = 0

@given('un radio de valor {radius}')
def step_impl(context, radius):
    radius = float(radius)

    global globalRadius
    globalRadius = radius
    assert globalRadius > 0

@when('al calcular el area')
def step_impl(context):
    pass

@then('el area es igual a ~{value} con un error absoluto menor que {absoluteErrorLine}')
def step_impl(context, value, absoluteErrorLine):
    value = float(value)
    absoluteErrorLine = float(absoluteErrorLine)
    
    global globalRadius
    area = radiusArea(globalRadius)
    absoluteError = abs(area - value)
    assert absoluteError < absoluteErrorLine