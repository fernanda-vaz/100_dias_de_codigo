def ceusius_fahrenheit(temp):
    fahrenheit = (temp * 9/5) + 32
    return fahrenheit
ceusius = float(input("Digite a temperatura em ceusius: "))
print(f"Temperatura em Fahrenheit: {ceusius_fahrenheit(ceusius)} ˚F")

# def ceusius_fahrenheit(ceusius):
#     fahrenheit = (ceusius * 9/5) + 32
#     return fahrenheit

# def fahrenheit_ceusius(fah):
#     ceusius = (32 - fah) * 5/9
#     return ceusius

# def converter_temperatura():
#     print("Escolha a operação: ")
#     print("1. Converter temperatura em Ceusius para Fahrenheit")
#     print("2. Converter a temperatura em Fahrenheit para Ceusius")

#     while True:
#         escolha = input("Escolha(1/2): ")

#         if escolha in ('1','2'):
#             temp = float(input("Qual a temperatura que deseja converter? "))

#             if escolha == '1':
#                 print("Resultado: ", ceusius_fahrenheit(temp), "˚F")
            
#             if escolha == '2':
#                     print("Resultado: ", fahrenheit_ceusius(temp), "˚C")
#         else:
#             print("Escolha inválida")
            
#         continuar = input("Deseja fazer outra conversão? (s/n)")

#         if continuar == "n":
#             print("Operação encerrada.")
#             break

# converter_temperatura()
