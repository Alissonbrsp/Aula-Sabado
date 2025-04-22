import random

n_rand = random.randint(1,10)

chances = 5
while chances > 0 :
    n_try = int(input("Adivine o número entre 1 e 10: "))

    if n_try > n_rand :
        print("O número é menor")
    elif n_try < n_rand :
        print("O número é maior")
    else :
        print("Você acertou")
        break
    chances -= 1
    
    if chances > 0 :
        print(f"Você ainda tem {chances} tentativas")
    else :
        print(f"Você perdeu! O número era {n_rand}")
        break
