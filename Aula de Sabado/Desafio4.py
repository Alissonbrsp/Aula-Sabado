c = int(input("Digite uma temperatura em graus Celsius: "))

def convert(c: int):
    r= (c * 1.8) + 32
    return r
    
f = convert(c)
print(f"{c}° Celsius é o mesmo que {f}° Fahrenheit")
