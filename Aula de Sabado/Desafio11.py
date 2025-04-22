a = 1
s = []

while a <= 100:
    if a % 2 == 0:
        s.append(a)
    a += 1
    
soma = sum(s)
print(soma)
