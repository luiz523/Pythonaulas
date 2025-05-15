dinheiro = 0
while dinheiro != -1:
    dinheiro = int(input("digite o valor que quer sacar:R$ "))
    if dinheiro > -1:
        nota100 = dinheiro // 100
        dinheiro = dinheiro-(nota100 * 100)
        nota50 = dinheiro//50
        dinheiro = dinheiro - (nota50 * 50)
        nota20 = dinheiro//20
        dinheiro= dinheiro-(nota20 * 20)
        nota10 = dinheiro//10
        dinheiro = dinheiro-(nota10 * 10)
        nota5 = dinheiro//5
        dinheiro = dinheiro-(nota5 * 5)
        nota1 = dinheiro//1
        dinheiro = dinheiro-(nota1 * 1)
        if nota100 != 0:
            print(f"{nota100} notas de R$: 100")
        if nota50 != 0:
            print(f"{nota50} notas de R$:50")
        if nota20 != 0:
            print(f"{nota20} notas de R$:20")
        if nota10 != 0:
            print(f"{nota10} notas de R$:10")
        if nota5 != 0:
            print(f"{nota5} notas de R$:5")
        if nota1 != 0:
            print(f"{nota1} notas de R$:1")