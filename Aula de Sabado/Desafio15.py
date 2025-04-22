pal = input("Digite uma palavra: ")
revert = pal[::-1]

if pal == revert:
    print("Essa palavra é um palíndromo")
else:
    print("Essa palavra não é um palíndromo")
