soma_pares = 0
soma_impares = 0
numero = 0

#numero = int(input("Digite um número positivo para classificar (ou negativo para sair):"))

while numero >= 0:
     
    if numero % 2 == 0:
        soma_pares = soma_pares + numero
        print(f"Numero {numero} é par")
        
    else:
        soma_impares = soma_impares + numero
        print(f"Numero {numero} é impar")
        
    numero = int(input("Digite outro número (ou um número negativo para sair)"))
        

print("Processo encerrado")
print(f"Soma total dos números PARES: {soma_pares}")
print(f"soma total dos números IMPARES: {soma_impares}")




        

    
