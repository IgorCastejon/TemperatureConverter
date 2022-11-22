from src.converters.consts import CELSIUS_ABSOLUTE_ZERO, CELSIUS_BELOW_ABSOLUTE_ZERO_ERROR_MESSAGE, FAHRENHEIT_ABSOLUTE_ZERO, FAHRENHEIT_BELOW_ABSOLUTE_ZERO_ERROR_MESSAGE, KELVIN_ABSOLUTE_ZERO, KELVIN_BELOW_ABSOLUTE_ZERO_ERROR_MESSAGE

class ConverterToCelsius():
    @staticmethod
    def convert_from_celsius(celsius):
        if celsius < CELSIUS_ABSOLUTE_ZERO:
            raise Exception(CELSIUS_BELOW_ABSOLUTE_ZERO_ERROR_MESSAGE)
        return celsius
    
    @staticmethod
    def convert_from_kelvin(kelvin):
        if kelvin < KELVIN_ABSOLUTE_ZERO:
            raise Exception(KELVIN_BELOW_ABSOLUTE_ZERO_ERROR_MESSAGE)
        return kelvin - 273.15
    
    @staticmethod
    def convert_from_fahrenheit(fahrenheit):
        if fahrenheit < FAHRENHEIT_ABSOLUTE_ZERO:
            raise Exception(FAHRENHEIT_BELOW_ABSOLUTE_ZERO_ERROR_MESSAGE)
        return (fahrenheit - 32) * (5.0 / 9.0)
