import os 
os.system("cls")
# #IF ENCADEADO -> TESTA TODAS AS CONDIÇÕES MESMO SE UMA FOR VERDADEIRA
# #ELIF -> TESTA TODAS AS CONDIÇÕES ATÉ UMA SER VERDADEIRA


# x = 15 

# if x <=20 :
#     print("entrou no if 14")
# if x <=15 :
#     print("entrou no if 15")
# if x <=16:
#     print("entrou no if 16")


# if x <=20:
#     print("entrou no if 14")
# elif x<=15:
#     print("entrou no if 15")
# elif x <=16:
#     print("entrou no if 16")


# # ESCREVA UM PROGRAMA EM PYTHON NA QUAL O USUARIO DIGITA A IDADE
# #  SE MENOR QUE 12 -> CRIANÇA
# #  SE MENOR QUE 18 -> ADOLESCENTE
# #  SE MENOR QUE 60 -> ADULTO
# #  SE NAO -> IDOSO


# # NO CASO SE USAR IF ELE VAI TESTAR TODAS AS CONDIÇÕES
# idade = int(input("digite sua idade: "))

# if idade < 12:
#     print("criança")
# if idade < 18:
#     print("adolescente")
# if idade< 60:
#     print("adulto")
# else: 
#     print("IDOSO")


# # SE USAR ELIF ELE VAI TESTAR UMA E SAIR DA ESTRUTURA
# if idade < 12:
#     print("criança")
# elif idade < 18:
#     print("adolescente")
# elif idade< 60:
#     print("adulto")
# else: 
#     print("IDOSO")

#Atividade 1
#replace("valor1", "valor2") -> substitui o valor 1 pelo valor 2
# nota1 = float(input("Coloque a primeira nota: ").replace(",", "."))
# nota2 = float(input("Coloque a segunda nota: ").replace(",","."))

# media = (nota1 + nota2)/2
# #:.2f -> formata para 2 casas decimais apenas no fstring({})
# print(f"média: {media:.2f}")
# if media < 5:
#     print("reprovado")
# elif media < 7:
#     print("em recuperação")
# elif media > 7:
#     print("Aprovado")

#atividade 2
# peso = float(input("digite seu peso: ").replace(",","."))
# altura = float(input("digite sua altura: ").replace(",","."))

# imc = peso/(altura*altura)
# print(f"seu imc é: {imc:.2f}")
# if imc < 17:
#     print("muito abaixo do peso")
# elif imc < 18.49:
#     print("abaixo do peso")
# elif imc <24.99:
#     print("peso normal")
# elif imc < 29.99:
#     print("acima do peso")
# elif imc < 34.99:
#     print("obesidade I")
# elif imc < 39.99:
#     print("obesidade II")
# else:
#     print("obesidade III(mórbida)")

#atividade 3
print("."*20,"AUTOCAR","."*20)
print(r""")
              .--.  .-"     "-.  .--.          
       / .. \/  .-. .-.  \/ .. \         
      | |  '|  /   Y   \  |'  | |        
      | \   \  \ 0 | 0 /  /   / |        
       \ '- ,\.-"`` ``"-./, -' /         
        `'-' /_   ^ ^   _\ '-'`          
        .--'|  \._   _./  |'--.          
      /`    \   \ `~` /   /    `\        
     /       '._ '---' _.'       \       
    /           '~---~'   |       \      
   /        _.             \       \     
  /   .'-./`/        .'~'-.|\       \    
 /   /    `\:       /      `\'.      \   
/   |       ;      |         '.`;    /   
\   \       ;      \           \/   /    
 '.  \      ;       \       \   `  /     
   '._'.     \       '.      |   ;/_     
jgs  /__&gt;     '.       \_ _ _/   ,  '--. 
   .'   '.   .-~~~~~-. /     |--'`~~-.  \
  // / .---'/  .-~~-._/ / / /---..__.'  /
 ((_(_/    /  /      (_(_(_(---.__    .' 
           | |     _              `~~`   
           | |     \'.                   
            \ '....' |                   
             '.,___.'                    
      """)
print("."*50)
print("TABELA DE REAJUSTE DE SALÁRIO:")
print(r"""
    Salários até R$ 2799,99 aumento de 20%;
    Salários entre R$ 2800,00 e R$6999,99 aumento de 15%;
    Salários entre R$ 7000,00 e R$ 14999,99 aumento de 10%;
    Salários de R$ 15000,00 em diante aumento de 5;
""")
salario = float(input("digite seu salário:R$ "))

if salario < 2799.99:
    p = 0.20
elif salario <6999.99:
    p = 0.15
elif salario < 14999.99:
    p = 0.10
else:
    p = 0.5

print("."*50)
print(f"seu salário antes do ajuste:R$ {salario}")
print(f"Seu porcentual de aumento: {p*100}%")
print(f"seu aumento é de :R$ {salario*p:.2f}")
print(f"Seu novo salario é de:R$ {salario*p+salario}")