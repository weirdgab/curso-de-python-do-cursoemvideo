temp = float(input('Qual a temperatura em Cº? '))
temp_convertido = temp * 1.8 + 32

print('A temperatura de {:.1f}°C corresponde a {:.1f}°F'.format(
    temp, temp_convertido))
