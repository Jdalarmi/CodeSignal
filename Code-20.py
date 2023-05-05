def solution(inputArray):  
    max_dif = 0
    for i in range(1, len(inputArray)):
        dif = abs(inputArray[i] - inputArray[i-1])
        if dif > max_dif:
            max_dif = dif
    return max_dif
        
    