def solution(inputString):
    freq = {}
    for i in inputString:
        freq[i] = freq.get(i, 0) + 1

    cont = 0
    for j in freq.values():
        if j % 2 == 1:
            cont += 1
        if cont > 1:
            return False
    return True

print(solution("aabb"))
