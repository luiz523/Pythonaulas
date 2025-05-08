import random, os
# papel = 1
# pedra = 2
# tesoura = 3

pessoa = input("Escolha entre Pedra, Papel e Tesoura: ").lower()
print("Pessoa")
match pessoa:
    case "papel":
        pessoa = 1
        print(r"""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
              """)
    case "pedra":
        pessoa = 2
        print(r"""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
              """)
    case "tesoura":
        pessoa = 3
        print(r"""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")
print("-"*40)
print("Maquina")
maquina = random.randint(1,3)
match maquina:
    case 1:
        print(r"""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
              """)
    case 2:
        print(r"""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
              """)
    case 3:
        print(r"""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")
print("-"*40)
resultado = pessoa - maquina
match resultado:
    case _ if pessoa == maquina:
        print("Empatou")
        os.system("color 9")
    case _ if resultado == 1 or maquina == 3:
        print("Ganhou")
        os.system("color 2")
    case _ if resultado == 2 or maquina == 1:
        print("Perdeu")
        os.system("color 4")
