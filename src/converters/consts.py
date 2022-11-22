CELSIUS = 'C'
KELVIN = 'K'
FAHRENHEIT = 'F'

SUPPORTED_TEMPERATURE_SCALES = [CELSIUS, KELVIN, FAHRENHEIT]

CELSIUS_ABSOLUTE_ZERO = -273.15
KELVIN_ABSOLUTE_ZERO = 0
FAHRENHEIT_ABSOLUTE_ZERO = -459.67

CELSIUS_BELOW_ABSOLUTE_ZERO_ERROR_MESSAGE = "O valor na escala de temperatura Celsius não pode ser menor que o zero absoluto ({} °C).".format(CELSIUS_ABSOLUTE_ZERO)
FAHRENHEIT_BELOW_ABSOLUTE_ZERO_ERROR_MESSAGE = "O valor na escala de temperatura Fahrenheit não pode ser menor que o zero absoluto ({} °F).".format(FAHRENHEIT_ABSOLUTE_ZERO)
KELVIN_BELOW_ABSOLUTE_ZERO_ERROR_MESSAGE = "O valor na escala de temperatura Kelvin não pode ser menor que o zero absoluto ({} K).".format(KELVIN_ABSOLUTE_ZERO)
