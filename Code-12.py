def solution(a):
    tam = len(a)
    posicao = []
    cont = 0
    for i in (a[0:tam]):
        if i == -1:
            cont = cont + 1
            posicao.append(cont)
        else:
            cont = cont + 1

    a.sort()
    listapositiva = []
    for n in a:
        if n > 0:
            listapositiva.append(n)

    for i in posicao:
        i = i - 1
        listapositiva.insert(i, (-1))

    return listapositiva