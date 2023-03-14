def solution(inputArray):
    vazia = [inputArray[i] * inputArray[i + 1] for i in range (0, len(inputArray) - 1)]
    return max(vazia)

