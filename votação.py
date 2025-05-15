nome1 = input("nome do candidato:")
numero1 = int(input("numero do candidato: "))
nome2 = input("nome do candidato: ")
numero2 = int(input("numero do candidato: "))
nome3 = input("nome do candidato: ")
numero3 = int(input("numero do candidato: "))
voto1 = 0
voto2 = 0
voto3 = 0
for pergunta in range (10):
   voto = int(input("digite o numero de candidato que quer votar "))
   if voto == numero1:
        voto1 = voto1 + 1
        print(f"você votou no candidadto {nome1}")
   elif voto == numero2:
     voto2 = voto2 + 1
     print(f"você votou no candidato {nome2}")
     if voto2 == 3 or voto2 == 6 or voto2 == 9:
        voto2 = voto2 + 1
   elif voto == numero3:
     voto3 = voto3 + 1
     print(f"você votou no {nome3}")
   else:
      print("banana")
print("-"*40)
print(f"candidato {nome1}, ganhou {voto1}")
print(f"candidato {nome2}, {voto2}")
print(f"candidato {nome3}, ganhou {voto3}")
print("-"*40)
ganhador = max(voto1, voto2, voto3)
if ganhador == voto1:
    print(f"o candidato {nome1} ganhou com {voto1} votos")
elif ganhador == voto2:
    print(f"o candidato {nome2} ganhou com {voto2}")
elif ganhador == voto3:
  print(f"o candidato {nome3} ganhou com {voto3} votos")
else:
   print("empate refaça a eleição")