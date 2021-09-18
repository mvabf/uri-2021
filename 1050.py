n = int(input())

ddd = [61, 71, 11, 21, 32, 19, 27, 31]

destination = [
    'Brasilia', 'Salvador', 'Sao Paulo', 'Rio de Janeiro', 'Juiz de Fora'
    , 'Campinas', 'Vitoria', 'Belo Horizonte'
]

for i in range(8):
    if (n not in ddd):
        print('DDD nao cadastrado')
        break

    if (n == ddd[i]):
       print(destination[i])
       break
    