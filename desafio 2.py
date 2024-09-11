def sequencia(x):
    a, b = 0, 1
    while a <= x:
        if a == x:
            return True
        a, b = b, a + b
    return False


x = int(input("digite um numero: "))
if sequencia(x):
    print(f"o número {x} pertence a sequência.")
else:
    print(f"o número {x} não pertence a sequência.")
