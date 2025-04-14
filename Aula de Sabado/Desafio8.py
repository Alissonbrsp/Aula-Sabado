#from datetime import datetime

#Verifica o ano atual
#agora = datetime.now()
#ano = int(agora.strftime("%Y"))

ano = int(input("Insira um ano: "))

def bissexto(ano):
    if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
        print(f"O ano de {ano} é bissexto")
    else:
        print(f"O ano de {ano} não é bissexto")
        
bissexto(ano)
