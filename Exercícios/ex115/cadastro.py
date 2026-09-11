from funcoes import cadastrar, leiaInt, leiaNome
from time import sleep
import json

try:
    with open('pessoas.txt', 'r', encoding='utf-8') as f:
        cadastro = json.load(f)
except:
    cadastro = list()

resp = 1
while True:
    print('-' * 60)
    print(f'{'MENU PRINCIPAL':^60}')
    print('-' * 60)
    print('\033[32m1 -\033[34m Ver pessoas cadastradas\033[m')
    print('\033[32m2 -\033[34m Cadastrar nova pessoa\033[m')
    print('\033[32m3 -\033[34m Sair do sistema\033[m')
    print('-' * 60)
    while True:
        resp = leiaInt('\033[32mSua Opção: \033[m')
        if resp < 4 and resp > 0:
            break
        print('\033[31mERRO! Por favor digite uma opção válida.\033[m')
    if resp == 3:
        print('-' * 60)
        print(f'{'SAINDO DO SISTEMA... ATÉ LOGO!':^60}')
        print('-' * 60)
        break
    elif resp == 2:
        print('-' * 60)
        print(f'{'NOVO CADASTRO':^60}')
        print('-' * 60)
        cadastrar(leiaNome('Nome: '), leiaInt('Idade: '), cadastro)
    else:
        print('-' * 60)
        print(f'{'PESSOAS CADASTRADAS':^60}')
        print('-' * 60)
        for c in cadastro:
            print(f'{c['Nome:']:<30} {c['Idade:']:>20} anos.')
    sleep(1)

with open('pessoas.txt', 'w', encoding='utf-8') as f:
    json.dump(cadastro, f, ensure_ascii=False, indent=4)