import sys
from src.converters.converter_to_celsius import ConverterToCelsius 
from src.converters.converter_to_fahrenheit import ConverterToFahrenheit 
from src.converters.converter_to_kelvin import ConverterToKelvin
from src.converters.consts import CELSIUS, KELVIN, FAHRENHEIT, SUPPORTED_TEMPERATURE_SCALES

expectedInputHelper = "Entrada esperada: {valor decimal na escala de temperatura de entrada} {escala de temperatura de entrada: C(elsius) | F(ahrenheit) | K(elvin)} {escala de temperatura de saída: C(elsius) | F(ahrenheit) | K(elvin)}"

def getInput():
    if (len(sys.argv) != 4):
        sys.exit(expectedInputHelper)
    
    valueFromTempScale = float(sys.argv[1])
    fromTemperatureScale = sys.argv[2]
    toTemperatureScale = sys.argv[3]

    if (fromTemperatureScale not in SUPPORTED_TEMPERATURE_SCALES or toTemperatureScale not in SUPPORTED_TEMPERATURE_SCALES):
        sys.exit(expectedInputHelper)
    return valueFromTempScale, fromTemperatureScale, toTemperatureScale

def convertTemperatureScale(valueFromTempScale, fromTemperatureScale, toTemperatureScale):
    if fromTemperatureScale == CELSIUS:
        return convertFromCelsiusTemperatureScale(valueFromTempScale, toTemperatureScale)
    if fromTemperatureScale == KELVIN:
        return convertFromKelvinTemperatureScale(valueFromTempScale, toTemperatureScale)
    if fromTemperatureScale == FAHRENHEIT:
        return convertFromFahrenheitTemperatureScale(valueFromTempScale, toTemperatureScale)

def convertFromCelsiusTemperatureScale(valueFromTempScale, toTemperatureScale):
    if toTemperatureScale == CELSIUS:
        return ConverterToCelsius.convert_from_celsius(valueFromTempScale)
    if toTemperatureScale == KELVIN:
        return ConverterToKelvin.convert_from_celsius(valueFromTempScale)
    if toTemperatureScale == FAHRENHEIT:
        return ConverterToFahrenheit.convert_from_celsius(valueFromTempScale)

def convertFromKelvinTemperatureScale(valueFromTempScale, toTemperatureScale):
    if toTemperatureScale == CELSIUS:
        return ConverterToCelsius.convert_from_kelvin(valueFromTempScale)
    if toTemperatureScale == KELVIN:
        return ConverterToKelvin.convert_from_kelvin(valueFromTempScale)
    if toTemperatureScale == FAHRENHEIT:
        return ConverterToFahrenheit.convert_from_kelvin(valueFromTempScale)

def convertFromFahrenheitTemperatureScale(valueFromTempScale, toTemperatureScale):
    if toTemperatureScale == CELSIUS:
        return ConverterToCelsius.convert_from_fahrenheit(valueFromTempScale)
    if toTemperatureScale == KELVIN:
        return ConverterToKelvin.convert_from_fahrenheit(valueFromTempScale)
    if toTemperatureScale == FAHRENHEIT:
        return ConverterToFahrenheit.convert_from_fahrenheit(valueFromTempScale)

def getFormatPrintTemperatureScale(temperatureScale):
    if temperatureScale == CELSIUS:
        return "°C"
    elif temperatureScale == FAHRENHEIT:
        return "°F"
    elif temperatureScale == KELVIN:
        return 'K'

def printConversionResult(valueFromTempScale, fromTemperatureScale, valueToTemperatureScale, toTemperatureScale):
    formatPrintFromTemperatureScale = getFormatPrintTemperatureScale(fromTemperatureScale)
    formatPrintToTemperatureScale = getFormatPrintTemperatureScale(toTemperatureScale)

    print("{} {} -> {} {}".format(valueFromTempScale, formatPrintFromTemperatureScale, valueToTemperatureScale, formatPrintToTemperatureScale))

if __name__ == '__main__':
    valueFromTempScale, fromTemperatureScale, toTemperatureScale = getInput()
    try:
        valueToTemperatureScale = convertTemperatureScale(valueFromTempScale, fromTemperatureScale, toTemperatureScale)
        printConversionResult(valueFromTempScale, fromTemperatureScale, valueToTemperatureScale, toTemperatureScale)
    except Exception as e:
        print(e)
