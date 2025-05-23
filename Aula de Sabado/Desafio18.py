def primo(n: int) -> bool:
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


num = int(input("Digite um número: "))

if primo(num):
    print(f"{num} é primo")
else:
    print(f"{num} não é primo")
