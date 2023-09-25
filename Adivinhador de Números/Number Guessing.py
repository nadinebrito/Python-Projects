import random

x = random.randrange(150)

tentativas = 0

tent = []

def Robo():
    novo = False
    
    while(True):
        x = random.randrange(150)
        
        if len(tent) != 0:
            for i in range(len(tent)):
                if x != tent[i]:
                    tent.append(x)
                    return x
        else:
            return x
    
    


while(True):
    #senha = int(input("Digite um número: "))

    senha = Robo()
    
    if (senha == x):
        tentativas +=1
        print("Parabéns você adivinhou! E com", tentativas, "tentativas.")
        break
    else:
        tentativas +=1
                
    



