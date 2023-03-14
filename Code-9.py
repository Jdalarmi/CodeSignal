def solution(inputArray):
    tam_palavra = max(len(s) for s in inputArray)
    lista_vazia = []
    for s in inputArray:
        if len(s) == tam_palavra:
            lista_vazia.append(s)
    return(lista_vazia)