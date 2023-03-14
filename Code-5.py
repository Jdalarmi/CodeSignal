def solution(n):
    if (n==1):
        return 1
    else:
        poli = 1
        for i in range(1, n + 1):
            poli = poli + i * 4 - 4
        return poli

