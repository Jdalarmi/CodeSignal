def solution(picture):
    n = len(picture[0]) + 2
    resultado = ['*' * n ]
    for i in picture:
        resultado.append('*' + i + '*')
    resultado.append('*' * n )
    return resultado
    



'''
picture = ["abc"]
n = len(picture[0]) + 2
resultado = ['*' * n ]
for i in picture:
    resultado.append('*' + i + '*')
resultado.append('*' * n )
'''