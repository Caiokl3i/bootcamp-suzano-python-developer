from unidade import metros_centimetros, celcius_fahrenheit, fahrenheit_celcius, centimetro_metros

metros = 15

centimetros = 2000

celcius = 38

fahrenheit = 55



print(f'{metros}m = {metros_centimetros(metros)}cm')

print(f'{centimetros}cm = {centimetro_metros(centimetros):.1f}m')

print(f'{celcius}C = {celcius_fahrenheit(celcius):.1f}F')

print(f'{fahrenheit}F = {fahrenheit_celcius(fahrenheit):.1f}C')
