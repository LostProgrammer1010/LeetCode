def conConstruct(ransomNote: str, magazine: str) -> bool:
    letter = dict()
    if len(magazine) < len(ransomNote):
        return False

    for i in magazine:
        if i not in letter:
            letter[i] = 1
        else:
            letter[i] += 1

    for i in ransomNote:
        if i not in letter:
            return False
        else:
            if letter[i] <= 0:
                return False
            letter[i] -= 1

    return True
