def lengthoflastword(s: str) -> int:
    s.strip()
    word = s.split(" ")
    word = [ c for c in word if c != ""]

    return len(word[len(word)-1])
