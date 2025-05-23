
# 12. Static Methods
# Assignment:
# Create a class TemperatureConverter with a static method celsius_to_fahrenheit(c) that returns the Fahrenheit value.\

class TemperaturConverter:

    @staticmethod
    def celcius_to_farenheit(c):
        return (c* 9/5) + 32

print(f'Temperature from celcius to farenheit is {TemperaturConverter.celcius_to_farenheit(20)}')