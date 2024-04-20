def isValid(s: str) -> bool:
    stack = []

    for p in s:
        match p:
            case '(': stack.append(')')
            case '[': stack.append(']')
            case '{': stack.append('}')
            case ')': 
                if not stack or stack.pop() != ')':
                    return False
            case ']': 
                if not stack or stack.pop() != ')':
                    return False
            case '}': 
                if not stack or stack.pop() != ')':
                    return False
    return not stack 
                
