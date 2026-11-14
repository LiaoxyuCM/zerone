true = True
false = False

def syntax_check(code: str) -> bool:
    stack: list[int] = [] # 0 -> if, 1 -> loop

    for char in code:
        if   char in ["0", "1"]: stack.append(0)
        elif char == ":": stack.append(1)
        elif char == ",":
            if not stack: return false
            if stack.pop() != 0: return false
        elif char == ";":
            if not stack: return false
            if stack.pop() != 1: return false

    return not stack
