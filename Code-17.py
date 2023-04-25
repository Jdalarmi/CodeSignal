lista = [2, 1, 10, 1]
tam = len(lista)
cont = 0
for i in range(1, tam):
    if lista[i] <= lista[i-1]:
        cont = cont + lista[i-1] - lista[i] + 1
        lista[i] = lista[i-1] + 1

print(cont)



