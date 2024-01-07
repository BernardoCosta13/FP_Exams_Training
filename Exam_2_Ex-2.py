def upperFirstLetters(s: str, n: int) -> list:
    words:list = [word for i,word in enumerate(s.split(" ")) if i % n == 0]
    
    return [word.capitalize() for word in words]

print(upperFirstLetters("hi there my friends of all places", 7))