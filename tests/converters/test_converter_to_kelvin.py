import unittest
from src.converters.converter_to_kelvin import ConverterToKelvin 

class TestConverterToKelvin(unittest.TestCase):
    
    def test_conversion_from_negative_celsius_to_kelvin_should_convert(self):
        celsius = -10
        kelvin = ConverterToKelvin.convert_from_celsius(celsius)
        self.assertAlmostEqual(263.15, kelvin)

    def test_conversion_from_zero_celsius_to_kelvin_should_convert(self):
        celsius = 0
        kelvin = ConverterToKelvin.convert_from_celsius(celsius)
        self.assertAlmostEqual(273.15, kelvin)

    def test_conversion_from_positive_celsius_to_kelvin_should_convert(self):
        celsius = 33
        kelvin = ConverterToKelvin.convert_from_celsius(celsius)
        self.assertAlmostEqual(306.15, kelvin)

    def test_conversion_from_zero_kelvin_to_kelvin_should_convert(self):
        kelvinIn = 0
        kelvinOut = ConverterToKelvin.convert_from_kelvin(kelvinIn)
        self.assertAlmostEqual(kelvinIn, kelvinOut)

    def test_conversion_from_positive_kelvin_to_kelvin_should_convert(self):
        kelvinIn = 10
        kelvinOut = ConverterToKelvin.convert_from_kelvin(kelvinIn)
        self.assertAlmostEqual(kelvinIn, kelvinOut)

    def test_conversion_from_negative_fahrenheit_to_kelvin_should_convert(self):
        fahrenheit = -40
        kelvin = ConverterToKelvin.convert_from_fahrenheit(fahrenheit)
        self.assertAlmostEqual(233.15, kelvin)

    def test_conversion_from_zero_fahrenheit_to_kelvin_should_convert(self):
        fahrenheit = 0
        kelvin = ConverterToKelvin.convert_from_fahrenheit(fahrenheit)
        self.assertAlmostEqual(255.372, kelvin, places=3)

    def test_conversion_from_positive_fahrenheit_to_kelvin_should_convert(self):
        fahrenheit = 32
        kelvin = ConverterToKelvin.convert_from_fahrenheit(fahrenheit)
        self.assertAlmostEqual(273.15, kelvin)

    def test_conversion_from_celsius_below_absolute_zero_to_kelvin_should_throw_exception(self):
        celsius = -400
        self.assertRaises(Exception, ConverterToKelvin.convert_from_celsius, celsius)

    def test_conversion_from_kelvin_below_absolute_zero_to_kelvin_should_throw_exception(self):
        kelvinIn = -1
        self.assertRaises(Exception, ConverterToKelvin.convert_from_kelvin, kelvinIn)

    def test_conversion_from_fahrenheit_below_absolute_zero_to_kelvin_should_throw_exception(self):
        fahrenheit = -600
        self.assertRaises(Exception, ConverterToKelvin.convert_from_fahrenheit, fahrenheit)
