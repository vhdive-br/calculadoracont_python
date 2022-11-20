from time import sleep
print('=' * 30,'Olá, bem vindo! Escolha sua opção desejada abaixo.','=' * 30)
print('=' * 31, 'Hello welcome! Choose your desired option below.','=' * 31)
sleep(1)
escolha = input('''
[ 1 ] Adição(Addition)
[ 2 ] Subtração(Subtraction)
[ 3 ] Divisão(Division)
[ 4 ] Multiplicação(Product)
Pressione/Press "Enter" ''')
while True:
    soma = 0
    menu = int(input('O que deseja? (Choose your option): '))
    sleep(1)
    print('Ok! Digite 0 para parar a calculadora (Enter 0 to stop the calculator).')
    while menu == 1:
        valor = int(input('Digite o valor (enter the value): '))
        soma = soma + valor
        print(soma)
        if valor == 0:
            break
    
    if menu == 0:1
        break
print('Fim! Obrigado volte sempre/Thank you and welcome back!')