import random
a = float(input("digite o primeiro numero: "))
b = float(input("digite o segundo numero: "))
opcao = 0
while opcao !=5:
    print("="*40)
    print("""
1-somar
2-multiplicar
3-maior
4-novo numero
5- sair do programa          
""")
    print("="*40)
    opcao = int(input("digite o que quer fazer: "))
    if opcao == 1:
        print(f"a soma de {a} + {b} é igual a {a+b}")
    elif opcao == 2:
        print(f"a multiplicação de {a} X {b} é igual a {a*b}")
    elif opcao ==3:
        maior = max(a,b)
        print(f"O maior numero entre {a} e {b} é {maior}")
    elif opcao == 4:
        a = random.randint(1,10)
        b = random.randint(1,10)
        print(f"Os novos numeros são {a} e {b}")
    elif opcao == 5:
        print("byeeeeeee")
        break
    else:
        print("numero invalido")
