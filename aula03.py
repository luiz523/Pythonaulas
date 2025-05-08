import os
os.system("cls")

#continuação input com int e float
#int() --> converte para inteiro
#float() --> converte para n quebrado
# numero = 10
# numero2 = int(input("digite um numero: "))
# print("o tipo de numero é,", type (numero2))
# print(f"soma de {numero} + {numero2} =", numero2 + numero)
#exemplo 2
# num1 = input("digite um numero:")
# soma = num1 + 10
# print("A soma de ", num1, "+", "15","=",soma)
#exemplo 3
# n1 = float(input("digite um numero: "))
# n2 = float(input("digite outro numero:"))

# soma = n1+n2

# print(f"a soma de {n1} + {n2} =", soma)

# #atividade
# n1 = float(input("digite o primeiro numero "))
# n2 = float(input("digite o segundo numero "))
# print(f"a multiplicação de {n1} * {n2} =", n1*n2)

# #atividade 2
# numero = int(input("digite um numero "))
# print("antecessor:", numero-1)
# print("sucessor", numero+1)

# #atividade 3
# idade = int(input("digite seu ano ne nascimento "))
# if idade >= 2025:
#  print("ano de nascimento incorreto")
# else:
#  print("atualmente você tem", 2025-idade)

#atividade 4
tm1 = input("nome do produto: ")
pr1 = float(input("praço do produto:R$ "))
tm2 = input("nome do produto: ")
pr2 = float(input("preço produto:R$ "))
ds1 = round(pr1*0.90,2)
ds2 = round(pr2*0.75,2)
print("="*9,"CAIXA","="*9)
print(f"o produto {tm1} custa R$ {pr1} com 10% de desconto custara R$ {ds1}")
print(f"o produto {tm2} custa R$ {pr2} com 25% de desconto custara R$ {ds2}")
print("-"*50)
total = ds1+ds2
print(f"preço total R$ {total}")

#round(valor,qtdcasasdecimais) ---> faz o arredondamento dos valores