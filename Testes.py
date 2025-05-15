import os
os.system("cls")
X = float(input("qual valor da pão? "))
for n in range(51):
    print(n, round(n*X,2))
quantidade = int(input("quantos pães você vai querer? "))
while quantidade >= 51:
 quantidade = int(input("não temos essa quantidade de pãos, digite uma nova quantidade: "))
 if quantidade <= 50:
  break
valor = quantidade*X
desconto = input("digite o codigo de desconto: ")
if desconto == ("raimundo"):
 descontado = valor*0.20
 valor = valor-descontado
else:
  print("desconto não encontrado")
dinheiro = input(f"vai dar R$ {valor} gostaria de pagar como? ")
if dinheiro == ("credito"):
 credito=  input("coloque a senha:")
elif dinheiro == ("drebito"):
 debrito = input("coloque a senha:")
elif dinheiro == ("dinheiro"):
 real = int(input("vai pagar com nota de quanto "))
 troco = real - valor
 if troco >= 0:
  float(print(f"seu troco é de R$ {troco}"))
senhas = input("obrigado pela compra ")
if senhas == ("mostrar"):
 print(f"cretido:{credito}, debito:{debrito}") 