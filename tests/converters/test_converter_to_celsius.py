import unittest
from src.converters.converter_to_celsius import ConverterToCelsius 

class TestConverterToCelsius(unittest.TestCase):

    def test_conversion_from_negative_celsius_to_celsius_should_convert(self):
        celsiusIn = -30
        celsiusOut = ConverterToCelsius.convert_from_celsius(celsiusIn)
        self.assertAlmostEqual(celsiusIn, celsiusOut)

    def test_conversion_from_zero_celsius_to_celsius_should_convert(self):
        celsiusIn = 0
        celsiusOut = ConverterToCelsius.convert_from_celsius(celsiusIn)
        self.assertAlmostEqual(celsiusIn, celsiusOut)

    def test_conversion_from_positive_celsius_to_celsius_should_convert(self):
        celsiusIn = 32
        celsiusOut = ConverterToCelsius.convert_from_celsius(celsiusIn)
        self.assertAlmostEqual(celsiusIn, celsiusOut)
    
    def test_conversion_from_zero_kelvin_to_celsius_should_convert(self):
        kelvin = 0
        celsius = ConverterToCelsius.convert_from_kelvin(kelvin)
        self.assertAlmostEqual(-273.15, celsius)

    def test_conversion_from_positive_kelvin_to_celsius_should_convert(self):
        kelvin = 300
        celsius = ConverterToCelsius.convert_from_kelvin(kelvin)
        self.assertAlmostEqual(26.85, celsius)

    def test_conversion_from_negative_fahrenheit_to_celsius_should_convert(self):
        fahrenheit = -40
        celsius = ConverterToCelsius.convert_from_fahrenheit(fahrenheit)
        self.assertAlmostEqual(-40, celsius)

    def test_conversion_from_zero_fahrenheit_to_celsius_should_convert(self):
        fahrenheit = 0
        celsius = ConverterToCelsius.convert_from_fahrenheit(fahrenheit)
        self.assertAlmostEqual(-17.7778, celsius, places=4)

    def test_conversion_from_positive_fahrenheit_to_celsius_should_convert(self):
        fahrenheit = 40
        celsius = ConverterToCelsius.convert_from_fahrenheit(fahrenheit)
        self.assertAlmostEqual(4.44444, celsius, places=5)
        
    def test_conversion_from_celsius_below_absolute_zero_to_celsius_should_throw_exception(self):
        celsius = -400
        self.assertRaises(Exception, ConverterToCelsius.convert_from_celsius, celsius)

    def test_conversion_from_kelvin_below_absolute_zero_to_celsius_should_throw_exception(self):
        kelvinIn = -1
        self.assertRaises(Exception, ConverterToCelsius.convert_from_kelvin, kelvinIn)

    def test_conversion_from_fahrenheit_below_absolute_zero_to_celsius_should_throw_exception(self):
        fahrenheit = -600
        self.assertRaises(Exception, ConverterToCelsius.convert_from_fahrenheit, fahrenheit)
