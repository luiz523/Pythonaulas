p = 0
saldo = 0
while p != 4:
    print("""
    1: Depositar
    2: Saque 
    3: Saldo da conta
    4: sair
    """)
    p = int(input("digite o que quer fazer: "))
    if p == 1:
        deposito = float(input("Digite o valor do deposito:R$ "))
        saldo= saldo + deposito
    elif p == 2:
        saque = float(input("Digite quanto quer sacar:R$ "))
        saldo = saldo - saque
    elif p == 3:
        print(f"Seu saldo é de R${saldo}")
    else:
        print("comando desconhecido")
else:
    print("Saio do programa")