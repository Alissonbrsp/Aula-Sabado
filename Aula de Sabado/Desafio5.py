def soma(a: int, b: int) :
    resultado = a + b
    return resultado
    
def subtracao(a: int, b: int) :
    resultado = a - b
    return resultado
    
def multiplicacao(a: int, b: int) :
    resultado = a * b
    return resultado
    
def divisao(a: int, b: int) :
    if b == 0 :
       return "Erro: divisão por zero"
    resultado = a / b
    return resultado

a = int(input("insira um número inteiro: "))
b = int(input("insira outro número inteiro: "))

sum = soma(a, b)
sub = subtracao(a, b)
mult = multiplicacao(a, b)
div = divisao(a, b)

print(f"{a} + {b} = {sum}")
print(f"{a} - {b} = {sub}")
print(f"{a} * {b} = {mult}")
print(f"{a} / {b} = {div}")
