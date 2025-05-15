# a = int(input("digite o 1 numero: "))
# b = int(input("digite o 2 numero: "))
# c = int(input("digite o 3 numero: "))
# d = int(input("digite o 4 numero: "))
# e = int(input("digite o 5 numero: "))
# numeros = [a, b, c, d, e]

# maior = max(numeros)
# print("O maior número da lista é:", maior)
namero = 0
maiornumero = 0
for macaco in range(5):
    numero = int(input("digite um numero "))
    if macaco ==0:
        maiornumero = numero
    if numero > maiornumero:
        maiornumero = numero
   
print(f"maior numero {maiornumero}")