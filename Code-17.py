lista = [2, 3, 3, 5, 5, 5, 4, 12, 12, 10, 15]
tam = len(lista)
cont = 0
for i in range(1, tam):
    if lista[i] <= lista[i-1]:
        cont = cont + lista[i-1] - lista[i] + 1
        lista[i] = lista[i-1] + 1

print(cont)



