def solution(statues):
    statues.sort()
    statues_total = []
    for i in range (statues[0], statues[-1]+1):
        statues_total.append(i)
    statues_final = set(statues_total) - set(statues)  
    return(len(statues_final))
    