from time import sleep
import emoji
print('=' * 30, 'Olá, bem vindo! Escolha sua opção desejada abaixo.', '=' * 30)
print('=' * 31, 'Hello welcome! Choose your desired option below.', '=' * 31)
sleep(1)
escolha = input('''
[ 1 ] Adição(Addition)
[ 2 ] Subtração(Subtraction)
[ 3 ] Divisão(Division)
[ 4 ] Multiplicação(Product)
Pressione/Press "Enter" ''')
for c in range(0, 4):
    menu = int(input('O que deseja? (Choose your option): '))
    sleep(1)
    while menu == 1:
        print('Digite 0 para parar/insert 0 to stop.')
        sleep(0.4)
        valor = int(input('Digite o valor (enter the value): '))
        soma = int(input('Digite a soma: '))
        if valor >= 1:
            valor = valor + soma
            print(valor)
        else:
            menu1 = int(input('O que deseja (Choose your option): '))
            if menu1 == 1:
                menu = 1
            if menu1 == 2:
                menu = 2
            if menu1 == 3:
                menu = 3
            if menu1 == 4:
                menu = 4
        '''if valor == 0:
            menu = int(input('O que deseja? (Choose your option): '))
            c = menu'''
    while menu == 2:
        sleep(0.4)
        print('Digite 0 para parar/insert 0 to stop.')
        valor = int(input('Digite o valor (enter the value): '))
        sub = int(input('Digite a subtração: '))
        if valor >= 1:
            valor -= sub
            print(valor)
        else:
            menu2 = int(input('O que deseja (Choose your option): '))
            if menu2 == 1:
                menu = 1
            if menu2 == 2:
                menu = 2
            if menu2 == 3:
                menu = 3
            if menu2 == 4:
                menu = 4
        '''if valor == 0:
            menu = int(input('O que deseja (Choose your option): '))
            c = menu'''
    while menu == 3:
        print('Digite 0 para parar/insert 0 to stop.')
        valor = int(input('Digite o valor (enter the value): '))
        div = int(input('Digite a divisão: '))
        if valor >= 1:
            valor //= div
            print(valor)
        else:
            menu3 = int(input('O que deseja (Choose your option): '))
            if menu3 == 1:
                menu = 1
            if menu3 == 2:
                menu = 2
            if menu3 == 3:
                menu = 3
            if menu3 == 4:
                menu = 4
        '''continuar = str(input('Deseja continuar? [S/N] '))
        if continuar == 'S':
            menu = 3
        if continuar == 'N':
            menu = int(input('O que deseja (Choose your option): '))
        if menu == 1:
            menu = 1
        if menu == 2:
            menu = 2
        if menu == 4:
            menu = 4'''
    while menu == 4:
        print('Digite 0 para parar/insert 0 to stop.')
        valor = int(input('Digite o valor (enter the value): '))
        multi = int(input('Digite a multiplicação: '))
        if valor >= 1:
            valor *= multi
            print(valor)
        else:
            menu4 = int(input('O que deseja (Choose your option): '))
            if menu4 == 1:
                menu = 1
            if menu4 == 2:
                menu = 2
            if menu4 == 3:
                menu = 3
            if menu4 == 4:
                menu = 4

print('Fim/End.')