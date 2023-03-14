def solution(matrix):
    linha = len(matrix)
    coluna = len(matrix[0])
    lista_coluna = []
    for c in range (coluna):
        col = []
        for l in range(linha):
            col.append(matrix[l][c])
        lista_coluna.append(col)

    soma = 0
    for i in lista_coluna:
        for n in i:
            if n == 0: break
            soma += n
    return soma