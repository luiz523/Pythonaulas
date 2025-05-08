import os
os.system("cls")
#ESTRUTURAS CONDICIONAIS IF ELSE (ELIF)
# SWITCH CASE -> (match case) escolha caso (a partir da versão 3.10)
# Match valor:
# case valor:

# linguagem = 100

# match linguagem:
#     case "python":
#         print("é facil")
#     case "java":
#         print("muito codigo, python faz com linhas menores")
#     case "c#":
#         print("massa")
#     case "js":
#         print("sou do back")
#     case "html":
#         print("kauan nao dorme")
#     case 10:
#         print("entrou aqui !")
#     case _:
#         print("outro caso")

#Atividade 1
# print("1:Segunda \n 2:Terça \n 3:Quarta \n 4:Quinta \n 5:Sexta \n 6:Sabado \n 7:Domingo")
# print("-"*40)
# d = int(input("Digite o numero do dia da semana: "))
# print("-"*40)
# match d:
    # case 1:
    #     print("segunda")
    # case 2:
    #     print("terça")
    # case 3:
    #     print("quarta")
    # case 4:
    #     print("quinta")
    # case 5:
    #     print("sexta")
    # case 6:
    #     print("sabado")
    # case 7:
    #     print("domingo")

#Atividade 2
# print("""
# 1- Xiomi 7S- R$15000,00
# 2- Iphone 15- R$50000,00
# 3- Sansung s25- R$6999,99
# FRETE:
#     SP -> R$ 40,00
#     RJ -> R$ 70,00
#     MG -> R$ 600,00
# """)
# c = float(input("Digite o numero do celular: "))
# f = input("Digite a sigla do estado: ").upper()
# match c:
#     case 1:
#         v = 15000.00
#     case 2:
#         v = 50000.00
#     case 3:
#         v = 6999.99
# match f:
#     case "SP":
#         frete = 40
#     case "RJ":
#         frete = 70
#     case "MG":
#         frete = 600
# print("-"*40)
# print(f"""
# Preço R$: {v}
# Frete R$: {frete}
# Total R$: {v + frete}
# """)

import random

# valor = 0
# #randint(valorinicial,valorfinal)
# valor = random.randint(0,100) #gera de 1 ate 99 aleatoriamente

# match valor:

#     case _ if valor <50 : 
#         print("menor que 50")
#     case _ if valor ==50:
#         print("= 50")
#     case _ if valor > 50:
#         print("maior que 50")


