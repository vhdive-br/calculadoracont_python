from time import sleep
print('=' * 30,'Olá, bem vindo! Escolha sua opção desejada abaixo.','=' * 30)
print('=' * 31, 'Hello welcome! Choose your desired option below.','=' * 31)
sleep(1)
escolha = input('''
[ 1 ] Adição(Addition)
[ 2 ] Subtração(Subtraction)
[ 3 ] Divisão(Division)
[ 4 ] Multiplicação(Product)''')
soma = 0
while True:
    menu = int(input('O que deseja? (Choose your option): '))
    sleep(1)
    print('Ok! Digite 0 para parar a calculadora (Enter 0 to stop the calculator).')
    while menu == 1:
        valor = int(input('Digite o valor (enter the value): '))
        if valor == 0:
            print(escolha)
        soma = soma + valor
        print(soma)
    
    if menu == 0:
        break
print('fim')