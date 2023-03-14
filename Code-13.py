def solution(inputString):
    stack = []
    for c in inputString:
        if c == ")":
            substring = ""
            while stack[-1] != "(":
                substring += stack.pop()[::-1]
            stack.pop()
            stack.append(substring)
        else:
            stack.append(c)
    return "".join(stack)

