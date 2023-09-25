import random


def Dice(x):
    while(True):
        num = random.randrange(x + 1)
        if(num != 0):
            return num 

while(True):

    res = input("Que dado vc quer roletar?")
    
    jogar = int(res)
    if(jogar%2==0 and jogar <= 20 and jogar != 14 and jogar != 16 and jogar != 18):
        print(Dice(jogar))

