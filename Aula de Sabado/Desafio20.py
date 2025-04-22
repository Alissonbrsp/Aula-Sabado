pessoas = {}
s = ""

while s != "não":
    
    s = input("Deseja adicionar alguém? ")
    
    if s == "sim":
        nome = input("Digite o nome: ")
        idade = int(input("Digite a idade: "))
        pessoas[nome] = idade
    elif s == "não":
        print("\nAs pessoas maiores de idade são: ")
        for nome, idade in pessoas.items():
            if idade >= 18:
                print(f"{nome} - {idade} anos")
        
    else:
        print("Entrada inválida")
    
