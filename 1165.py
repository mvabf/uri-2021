qtd = int(input())

for x in range(qtd):
    n = int(input())
    divisores = 0
    for i in range(1, n + 1, 1):
        if (n % i == 0):
            divisores+=1

    if (divisores > 2):
        print(f'{n} nao eh primo')
    else:
        print(f'{n} eh primo')