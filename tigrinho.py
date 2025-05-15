import random
import time
import os
os.system("cls")
print("-"*40)
print("      BANANA BET")
print("-"*40)
#saca
#deposita
#sair
#jogar
macaco = print(r"""
            __,__           
   .--.  .-"     "-.  .--.  
  / .. \/  .-. .-.  \/ .. \ 
 | |  '|  /   Y   \  |'  | |
 | \   \  \ 0 | 0 /  /   / |
  \ '- ,\.-"`` ``"-./, -' / 
   `'-' /_   ^ ^   _\ '-'`  
       |  \._   _./  |      
       \   \ `~` /   /      
        '._ '-=-' _.'       
           '~---~'          
    """)
m = 0
bananas = 0.0
while m != 2:
    print("-"*40)
    print(" 1:Depositar \n 2:Jogar \n 3:Sair \n 4:Sacar")
    print(f"saldo de bananas: {bananas}")
    print("-"*40)
    m = int(input("digite oque deseja fazer: "))
    print("-"*40)
    if m == 1:
        bananas = float(input("Quantas bananas você deseja depositar: "))
        print(f"{bananas}")
        continue
    elif m == 4:
       if bananas == 0:
            print("você não tem bananas para sacar, por favor deposite bananas para jogar e ganhar mais bananas ;)")
            time.sleep(1)
       else:
        sacado = float(input(f"você tem {bananas} bananas, gostaria de sacar tudo ou só uma parte? Digite quanto você quer sacar: "))
        print(f"Você quer sacar {sacado} bananas, nossa casa de investimentos pega uma parte dessas bananas para se manter ativo")
        roubo = sacado*0.25
        print(f"Você sacou {roubo} bananas")
        bananas = bananas - sacado
        time.sleep(1)
    if bananas != 0:
        print("*"*40)
        print("HORA DE JOGAR")
        print("*"*40)
        aposta = float(input("Gostaria de apostar quanto? "))
        tentativas = bananas/aposta
        giros = int(input("Ira girar quantas vezes? "))
        # giros = giros - 1


        print("-"*40)
        while giros != 0:
            time.sleep(1)
            giros = giros - 1
            os.system("color 7")
            if bananas <= 0:
                print("acabou suas bananas coloque mais :)")
                break
            print(f"Você tem {giros+1} restantes")
            primeiro = random.randint(1,3)
            if primeiro == 1:
                print(r"""
                .-.  
            /  |  
            |  /   
        .'\|.-; _ 
        /.-.;\  |\|
        '   |'._/ `
            |  \   
            \  |  
                '-'
                    """)

            elif primeiro == 2:
                print(r"""
                    __,__           
        .--.  .-"     "-.  .--.  
        / .. \/  .-. .-.  \/ .. \ 
        | |  '|  /   Y   \  |'  | |
        | \   \  \ 0 | 0 /  /   / |
        \ '- ,\.-"`` ``"-./, -' / 
        `'-' /_   ^ ^   _\ '-'`  
            |  \._   _./  |      
            \   \ `~` /   /      
                '._ '-=-' _.'       
                '~---~'          
            """)
            elif primeiro == 3:
                print(r"""
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
            print("-"*40)
            time.sleep(1)
            segundo = random.randint(1,3)
            if segundo == 1:
                print(r"""
                .-.  
            /  |  
            |  /   
        .'\|.-; _ 
        /.-.;\  |\|
        '   |'._/ `
            |  \   
            \  |  
                '-'
            """)
            elif segundo == 2:
                print(r"""
                    __,__           
        .--.  .-"     "-.  .--.  
        / .. \/  .-. .-.  \/ .. \ 
        | |  '|  /   Y   \  |'  | |
        | \   \  \ 0 | 0 /  /   / |
        \ '- ,\.-"`` ``"-./, -' / 
        `'-' /_   ^ ^   _\ '-'`  
            |  \._   _./  |      
            \   \ `~` /   /      
                '._ '-=-' _.'       
                '~---~'          
            """)
            elif segundo == 3:
                print(r"""
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
            print("-"*40)
            time.sleep(1)
            terceiro = random.randint(1,3)
            if terceiro == 1:
                print(r"""
                .-.  
            /  |  
            |  /   
        .'\|.-; _ 
        /.-.;\  |\|
        '   |'._/ `
            |  \   
            \  |  
                '-'
            """)
            elif terceiro == 2:
                print(r"""
                    __,__           
        .--.  .-"     "-.  .--.  
        / .. \/  .-. .-.  \/ .. \ 
        | |  '|  /   Y   \  |'  | |
        | \   \  \ 0 | 0 /  /   / |
        \ '- ,\.-"`` ``"-./, -' / 
        `'-' /_   ^ ^   _\ '-'`  
            |  \._   _./  |      
            \   \ `~` /   /      
                '._ '-=-' _.'       
                '~---~'          
            """)
            elif terceiro == 3:
                print(r"""
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
            print("-"*40)
            time.sleep(2)
            if terceiro == segundo and segundo == primeiro:
                print("Ganhou")
                bananas = bananas + (2*aposta)
                print(f"bananas: {bananas}")
                os.system("color 2")
                time.sleep(4)
            else:
                print("Perdeu")
                bananas = bananas - aposta
                print(f"bananas: {bananas}")
                os.system("color 4")
                time.sleep(4)
    m=0
    if bananas == 0:
        print("Você não tem mais Bananas ;-; coloque mais para jogar")