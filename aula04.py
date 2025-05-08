#ESTRUTURA CONDICIONAL IF ELSE (se senao) -> True or False (Verdadeiro ou Falso)
#OPERADORES CONDICIONAIS:  > >= < <= != == and or
# > (maior)
# >= ( maior OU igual)
# < (menor)
# <= (menor OU igual)
# == (igual) 
# != (diferente)
# and (e) -> Se apenas uma ou mais condiçoes for FALSA ele retorna FALSE 
# or (ou) -> Se apenas uma ou mais condições for VERDADE ele retorna TRUE

#if condicao :
# print("verdade")
#else: 
#print("falso")

# A IDENTAÇÃO (ESPAÇO) deve ser utilizado o TAB

# x=10  

# if x > 1000:
#     print("verdade")
# else:
#     print("falso")
#     print("falso")
#     print("falso")
#     print("falso")

# nome = "teste"
# if "testee" != nome:
#     print(1)
# else:
#     print(2)

#atividade 1 e 2
# idade = int(input("Qual a sua idade? "))
# if idade <= 0 or idade <= 120:
#     print("sua idade tem que ser entre 0 e 120")
# else:
#     if idade > 18:
#         print("maior")
#     else:
#          print("menor")

# #atividade 3
# gmail = input("Gmail: ")
# senha = input("Senha: ")
# if gmail == ("python@senai.com") and senha == ("12345678"):
#     print("usuario autenticado")
# else:
#     print("usuario ou senha incorreta")

# maça = int(input("quantas maças você quer? "))
# preço = 0.30
# if maça >= 12:
#     preço = 0.25
# print(f"{maça} maças: R$ {preço} unidade, total -> R$ {maça*preço}")

# #atividade 5
# letra = input("digite uma letra: ")
# if letra == "a" or letra == "e" or letra == "i" or letra =="o" or letra =="u":
#     print(f"a letra: {letra} é vogal")
# else:
#     print(f"a letra {letra} é consoante")

# #atividade 5
# n1 = int(input("digite um numero: "))
# n2 = int(input("digite outro numero: " ))
# if n1 < n2:
#     print(f"maior numero: {n2}")
#     print(f"menor numero: {n1}")
# else:
#     print(f"maior numero: {n1}")
#     print(f"menor numero: {n2}")

#reescrevendo de outra maneira
#upper() --> converter tudo para maiusculo
#lower() --> converter tudo para minusculo
# letra = input("digite uma letra: ").lower()
# if letra == "a" or letra == "e" or letra == "i" or letra =="o" or letra =="u":
#     print(f"a letra: {letra} é vogal")
# else:
#     print(f"a letra {letra} é consoante")

#reescrevendo de outra maneira
# AND(E) OR(OU) in(DENTRO --> apenas para string)
# letra = input("digite uma letra: ")
# if letra in "aeiouAEIOU":
#     print(f"a letra: {letra} é vogal")
# else:
#     print(f"a letra {letra} é consoante")