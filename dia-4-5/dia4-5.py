def adicao(x, y):
    return x+y

def subtracao(x, y):
    return x-y

def divisao(x, y):
    return x/y

def multiplicacao(x, y):
    return x*y

def calculadora():
    print("Selecione a operação: ")
    print("1.Adicao")
    print("2.Subtracao")
    print("3.Divisao")
    print("4.Divisao")

    while True:
        escolha = input("Escolha(1/2/3/4): ")

        if escolha in ('1', '2', '3', '4'):
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Dogite o segundo número: "))

            if escolha == '1':
                print("Resultado: ", adicao(num1, num2))

            if escolha == '2':
                print("Resultado: ", subtracao(num1, num2))
            
            if escolha == '3':
                if num2 != 0:
                    print("Resultado: ", divisao(num1, num2))
                else:
                    print("Não é permitida a divisão por 0")
            if escolha == '4':
                print("Resultado: ", multiplicacao(num1, num2))
        else:
            print("Escolha inválida")

        continuar = input("Deseja fazer outra operação? (s/n)")

        if continuar == "n":
            print("Calculadora encerrada.")
            break

calculadora()