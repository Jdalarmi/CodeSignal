def solution(yourLeft, yourRight, friendsLeft, friendsRight):
    if yourLeft == friendsRight and yourRight == friendsLeft:
        return True
    elif yourLeft == friendsLeft and yourRight == friendsRight:
        return True
    elif yourLeft == friendsLeft and yourRight > friendsRight:
        return False
    elif yourLeft > friendsLeft or yourRight < friendsRight:
        return False
    else:
        return False
    
print(solution(1, 10, 10, 0))