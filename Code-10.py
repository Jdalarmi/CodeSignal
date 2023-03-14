def solution(s1, s2):
    letra_comuns = 0
    for i in set(s1):
        letra_comuns += min(s1.count(i), s2.count(i))
    return letra_comuns