def containsConsecutive(listP: list[list]) -> bool:
    nrVerify = [i + 1 for i in range(len(listP)**2)]
    consecutive_list: list = [number for sublist in listP for number in sublist]
    
    return sorted(nrVerify) == sorted(consecutive_list)
