from datetime import date

print('-' * 20)
print('\033[1mPrograma de Classificação da \033[1;34mConfederação Brasileira de Natação\033[m')
print('-' * 20)

anoNascimento = int(input('Digite seu ano de nascimento: '))
anoAtual = date.today().year
idade = anoAtual - anoNascimento

if idade < 8 and idade >= 5:
    print('Você é um atleta classificado como \033[34mPRÉ-MIRIM\033[m')
elif idade >= 9 and idade < 11:
    print('Você é um atleta classificado como \033[34mMIRIM\033[m')
elif idade >= 11 and idade < 13:
    print('Você é um atleta classificado como \033[34mPETIZ\033[m')
elif idade >= 13 and idade < 15:
    print('Você é um atleta classificado como \033[34mINFANTIL\033[m')
elif idade >= 15 and idade < 17:
    print('Você é um atleta classificado como \033[34mJUVENIL\033[m')
elif idade >= 17 and idade < 20:
    print('Você é um atleta classificado como \033[34mJÚNIOR\033[m')
elif idade > 20:
    print('Você é um atleta classificado como \033[34mSÊNIOR\033[m')
elif idade < 5 and idade >= 0:
    print('Você não tem idade suficiente para fazer a modalidade.')
elif idade < 0:
    print('Anos que ainda não ocorreram não são permitidos no programa.')