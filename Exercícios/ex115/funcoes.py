def leiaInt(msg):
    while True:
        try:
            nome = int(input(msg))
            return nome
        except KeyboardInterrupt:
            print('\n\033[31mERRO! O usuário encerrou o programa.\033[m')
            return 0
        except:
            print('\033[31mERRO! Por favor digite um número inteiro válido.\033[m')
        else:
            break


def leiaNome(msg):
    while True:
        nome = str(input(msg)).strip()
        nome1 = nome.replace(' ', '')
        if nome1.isalpha():
            return nome
            break
        else:
            print('\033[31mERRO! Por favor digite um nome válido!\033[m')

def cadastrar(nome, idade, lista=None):
    if lista is None:
        lista = list()
    dicionario = dict()
    dicionario['Nome:'] = nome
    dicionario['Idade:'] = idade
    lista.append(dicionario.copy())
    print(f'Novo registro de {dicionario['Nome:']} adicionado.')
    dicionario.clear()
    return lista
