def ficha(gols=0, nome='<desconhecido>'):
    if gols == int or gols == float:
        return f'O jogador {nome} fez {gols} gol(s) no campeonato.'
    else:
        gols = 0
        return f'O jogador {nome} fez {gols} gol(s) no campeonato.'


n = str(input('Nome do Jogador: '))
g = input('Número de Gols: ')
print(ficha(g, n))
