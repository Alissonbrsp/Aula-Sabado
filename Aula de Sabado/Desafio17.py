def media (a, b):
    r = (a + b) / 2
    return r

a = int(input("insira um número: "))
b = int(input("insira mais um número: "))

m = media(a, b)

print(f"A média dos números {a} e {b} é {m}")
