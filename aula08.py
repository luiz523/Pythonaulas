import os
os.system("cls")
#estrutura de repetição while (enquanto)
#enquanto uma condição for  verdadeiro ele executa o looping até que ela seja falsa

# aula = 8
# while aula ==8:
#     print("silencio")
# #     aula=9
# # else:
# #     print("é executado quando o while é falso")

#     # while incremental
# i=0

# while i <10:
#     # i = i+i incrementaar de 1 em 1
#     i+=1 #incremento simplificado mesma coia que i = i+1
#     print("valor da variavel = ", i)

#atividade 1
# i=2
# while i <19:
#     print(f"{i}")
#     i+=1

 #atividade 2
# i=0
# while i>-51:
#     print(f"{i}")
#     i-=1

#atividade 3
i=0
while i != 4:
    print("""
1 - cadastrar o nome
2 - cadastrar o cpf
3 - cadastrar a idade
4 - sair
""")
    i = int(input("Digite oque quer fazer primeiro: "))
    if i == 1:
        nome = input("Digite seu nome completo: ")
    if i == 2:
        cpf = int(input("Digite seu cpf: "))
    if i == 3:
        idade = int(input("digite sua idade: "))
    else:
        print("numero invalido")
    
print(f"""
***************Usuario***************
Nome: {nome}
cpf: {cpf}
idade: {idade}
************************************
""")