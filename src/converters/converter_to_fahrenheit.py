from src.converters.consts import CELSIUS_ABSOLUTE_ZERO, CELSIUS_BELOW_ABSOLUTE_ZERO_ERROR_MESSAGE, FAHRENHEIT_ABSOLUTE_ZERO, FAHRENHEIT_BELOW_ABSOLUTE_ZERO_ERROR_MESSAGE, KELVIN_ABSOLUTE_ZERO, KELVIN_BELOW_ABSOLUTE_ZERO_ERROR_MESSAGE

class ConverterToFahrenheit:
    @staticmethod
    def convert_from_celsius(celsius):
        if celsius < CELSIUS_ABSOLUTE_ZERO:
            raise Exception(CELSIUS_BELOW_ABSOLUTE_ZERO_ERROR_MESSAGE)
        return (celsius * (9.0 / 5.0)) + 32 
    
    @staticmethod
    def convert_from_kelvin(kelvin):
        if kelvin < KELVIN_ABSOLUTE_ZERO:
            raise Exception(KELVIN_BELOW_ABSOLUTE_ZERO_ERROR_MESSAGE)
        return ((9.0 / 5.0) * (kelvin - 273.15)) + 32
    
    @staticmethod
    def convert_from_fahrenheit(fahrenheit):
        if fahrenheit < FAHRENHEIT_ABSOLUTE_ZERO:
            raise Exception(FAHRENHEIT_BELOW_ABSOLUTE_ZERO_ERROR_MESSAGE)
        return fahrenheit