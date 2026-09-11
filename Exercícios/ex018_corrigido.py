import math

an = float(input('Digite o ângulo que você deseja: '))
sen = math.sin(math.radians(an))
cos = math.cos(math.radians(an))
tan = math.tan(math.radians(an))

print('O ângulo de {} possui o seno de {:.2f} e o cosseno de {:.2f} e a tangente de {:.2f}.'.format(
    an, sen, cos, tan))