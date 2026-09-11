from datetime import datetime


def voto(n):
    if n >= 18 and n <= 70:
        return f'Com {n} anos: VOTO OBRIGATÓRIO.'
    elif n < 16:
        return f'Com {n} anos: VOTO NEGADO.'
    else:
        return f'Com {n} anos: VOTO OPCIONAL.'


ano = int(input('Em que ano você nasceu? '))
idade = datetime.now().year - ano

print(voto(idade))
