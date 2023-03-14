def solution(n):
    n = str(n)
    tam = len(n)
    valor = tam // 2
    lista1 = []
    lista2 = []
    for i in (n[0:valor]):
        lista1.append(int(i))
    for r in (n[valor:tam]):
        lista2.append(int(r))
    v1 = 0
    v2 = 0
    for s in (lista1):
        v1 = v1 + int(s)
    for f in (lista2):
        v2 = v2 + int(f)
        
    if v1 == v2:
        return(True)
    else:
        return(False)