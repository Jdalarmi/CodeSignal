def solution(a):
    peso = a
    equipe1 = []
    equipe2 = []
    cont = 0
    for i in range(0, len(peso), 2):
        equipe1.append(peso[i])
    for i in range(1, len(peso), 2):
        equipe2.append(peso[i])
    valor_final = []
    soma1 = 0
    soma2 = 0
    for i in equipe1:
        soma1 += i 
    valor_final.append(soma1)
    for i in equipe2:
        soma2 += i
    valor_final.append(soma2)

    return valor_final