frase = input("Digite uma frase: ").lower()
vogais = "aeiou"
qnt = 0

for v in frase:
    if v in vogais:
        qnt += 1
        
print(f"Há {qnt} vogais nessa frase")
