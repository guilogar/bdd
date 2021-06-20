Feature: circle
  Scenario: Calcular area
    Given un radio de valor 5.0
    When al calcular el area
    Then el area es igual a ~78.54 con un error absoluto menor que 0.1