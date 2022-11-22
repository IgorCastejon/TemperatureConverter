import unittest
from src.converters.converter_to_fahrenheit import ConverterToFahrenheit

class TestConverterToKelvin(unittest.TestCase):
    
    def test_conversion_from_negative_celsius_to_fahrenheit_should_convert(self):
        celsius = -40
        fahrenheit = ConverterToFahrenheit.convert_from_celsius(celsius)
        self.assertAlmostEqual(-40, fahrenheit)

    def test_conversion_from_zero_celsius_to_fahrenheit_should_convert(self):
        celsius = 0
        fahrenheit = ConverterToFahrenheit.convert_from_celsius(celsius)
        self.assertAlmostEqual(32, fahrenheit)

    def test_conversion_from_positive_celsius_to_fahrenheit_should_convert(self):
        celsius = 10
        fahrenheit = ConverterToFahrenheit.convert_from_celsius(celsius)
        self.assertAlmostEqual(50, fahrenheit)

    def test_conversion_from_zero_kelvin_to_fahrenheit_should_convert(self):
        kelvin = 0
        fahrenheit = ConverterToFahrenheit.convert_from_kelvin(kelvin)
        self.assertAlmostEqual(-459.67, fahrenheit)

    def test_conversion_from_positive_kelvin_to_fahrenheit_should_convert(self):
        kelvin = 300
        fahrenheit = ConverterToFahrenheit.convert_from_kelvin(kelvin)
        self.assertAlmostEqual(80.33, fahrenheit)

    def test_conversion_from_negative_fahrenheit_to_fahrenheit_should_convert(self):
        fahrenheitIn = -40
        fahrenheitOut = ConverterToFahrenheit.convert_from_fahrenheit(fahrenheitIn)
        self.assertAlmostEqual(fahrenheitIn, fahrenheitOut)

    def test_conversion_from_zero_fahrenheit_to_fahrenheit_should_convert(self):
        fahrenheitIn = 0
        fahrenheitOut = ConverterToFahrenheit.convert_from_fahrenheit(fahrenheitIn)
        self.assertAlmostEqual(fahrenheitIn, fahrenheitOut)

    def test_conversion_from_positive_fahrenheit_to_fahrenheit_should_convert(self):
        fahrenheitIn = 32
        fahrenheitOut = ConverterToFahrenheit.convert_from_fahrenheit(fahrenheitIn)
        self.assertAlmostEqual(fahrenheitIn, fahrenheitOut)

    def test_conversion_from_celsius_below_absolute_zero_to_fahrenheit_should_throw_exception(self):
        celsius = -400
        self.assertRaises(Exception, ConverterToFahrenheit.convert_from_celsius, celsius)

    def test_conversion_from_kelvin_below_absolute_zero_to_fahrenheit_should_throw_exception(self):
        kelvinIn = -1
        self.assertRaises(Exception, ConverterToFahrenheit.convert_from_kelvin, kelvinIn)

    def test_conversion_from_fahrenheit_below_absolute_zero_to_fahrenheit_should_throw_exception(self):
        fahrenheit = -600
        self.assertRaises(Exception, ConverterToFahrenheit.convert_from_fahrenheit, fahrenheit)
