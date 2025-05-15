import random
numero = 1
escolga = 0 
while escolga != numero:
    numero = random.randint(1,10)
    escolga = int(input("digite um numero: "))
    if escolga != numero:
        print(f"""
Maquina escolheu: {numero}
Você escolheu: {escolga}
ERRRRROUUUUUUUU
""")
    else:
        print(f"""
Maquina escolheu: {numero}
Você escolheu: {escolga}
Acertou ;-;
""")
        