Feature: circle

  Scenario Outline: Calcular area
    Given un radio de <radius> m
    When al calcular el area
    Then devuelve un valor aproximado a <result> m con un error absoluto de <error>

    Examples:
      | radius | result | error |
      | 5      | 78.5   | 0.1   |
      | 6      | 113.04 | 0.1   |
  
  Scenario Outline: Calcular area negativa
    Given un radio de <radius> m
    When al calcular el area, se lanza una exception de tipo InvalidRadius

    Examples:
      | radius |
      |  0     |
      | -5     |
      | -6     |