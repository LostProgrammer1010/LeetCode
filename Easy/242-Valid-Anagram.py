def ifAnagram(s: str, t: str) -> bool:
    character = dict()
    if len(s) != len(t):
        return False

    for i in s:
        if not i in character:
            character[i] = 1
        else:
            character[i] += 1
 
    for i in t:
        if not i in character:
            return False
        if character[i] == 0:
            return False
        character[i] += 1           
        
    return True
