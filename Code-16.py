a = [832, 998, 148, 570, 533, 561, 894, 147, 455, 279]
b = [832, 570, 148, 998, 533, 561, 455, 147, 894, 279]
  
if a == b:
    print(True)

diferente = [(i, j) for i, j in zip(a, b) if i != j]
if len(diferente) != 2:
    print(False)
if diferente [0][0] == diferente[1][0] and diferente[0][1] == diferente[1][1]:
    print(True)
if diferente[0][0] == diferente[1][1] and diferente[0][1] == diferente[1][0]:
    print(True)
print(False)