nota = input('Digite a primeira nota do aluno: ')
nota2 = input('Digite a segunda nota do aluno: ')

if nota.isnumeric() == False:
    print('Valor digitado não reconhecido. Por favor reinicie o programa.')
else:
    if nota2.isnumeric() == False:
        print('Valor digitado não reconhecido. Por favor reinicie o programa.')
    else:
        nota = float(nota)
        nota2 = float(nota2)
        media = (nota + nota2) / 2
        if media < 5:
            print('Aluno \033[31mREPROVADO\033[m')
        elif media >= 5 and media <= 6.9:
            print('Aluno de \033[33mRECUPERAÇÃO\033[m')
        else:
            print('Aluno \033[32mAPROVADO\033[m')