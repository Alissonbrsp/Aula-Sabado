estoque = {"arroz":3}
opcao = 0 # inicia 

while opcao != 3:
    
    
    print("Menu")
    print("1-Adicionar Produto")
    print("2-Consultar Produto")
    print("3-Sair")
    
    exiba = int(input("Escolha sua opção:"))
    
    if exiba == 1:
        nome = input("Digite o nome do produto:")
        quantidade = input("Digita a quantidade:")
        
    if nome == estoque:
        estoque[arroz] = estoque[arroz] + quantidade
        print(f"{quantidade}")
        
        
        
    
        
    
     
            
            

    
    