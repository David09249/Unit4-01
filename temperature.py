# Created by: David Wang
# Created on: 30-Oct-2017
# Created for: ICS3U
# Daily Assignment - Unit4-01
# This program displays temperature in degrees Fahrenheit, given degrees Celcius

print('Enter a Temprature in Degrees Celsius')
celsius = float(raw_input())

def calculate_fahrenheit(celsius_input):
	
    fahrenheit = 1.8 * celsius_input + 32
    
    print(str(fahrenheit) + unichr(176) + " Fahrenheit is the converted from " + str(celsius_input) + unichr(176) + " Celsius")

calculate_fahrenheit(celsius)
