lista = [1, 4, 10, 6, 2]
max_lista = max(lista)

for i in range(1, max_lista+2, 1):
    numero_de_elementos = round(max_lista/i)
    lista_nova = []
    for j in range(i, max_lista + 2, i):
        lista_nova.append(j)
    a = set(lista)
    b = set(lista_nova)

    if not len(a.intersection(b)): # {4, 6, 10}
        break
print(i)

