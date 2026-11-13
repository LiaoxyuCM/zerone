# // Transfer JS into Python, a bit incompatible
true = True
false = False

def zerone_exec(code: str):
    result: list[bool] = [false]
    cursor: int = 0
    code = code.strip()
    code_cursor: int = 0
    skipinside: bool = false
    skipstack: int = 1
    loops: list[tuple[int, int]] = []
    loopmark: list[int] = []

    while code_cursor < len(code):
        char = code[code_cursor]
        if not skipinside:
            match char:
                case "!": result[cursor] = not result[cursor]
                case "<":
                    if cursor == 0: result.insert(0, false)
                    else: cursor -= 1
                case ">":
                    if cursor == (len(result)-1): result.append(false)
                    cursor += 1
                case "^": cursor = 0
                case "$": cursor = len(result)-1
                case "0": skipinside = result[cursor]
                case "1": skipinside = not result[cursor]
                case ":": loopmark.append(code_cursor)
                case ";":
                    if loopmark:
                        loops.append((loopmark[-1], code_cursor))
                        code_cursor = loopmark[-1]
                        loopmark.pop()
                    elif loops[-1][1] == code_cursor:
                        code_cursor = loops[-1][0]
                case "_":
                    code_cursor = loops[-1][1]
                    loops.pop()

        else:
            if char in ["0", "1", ":"]: skipstack += 1
            elif char in [",", ";"]: skipstack -= 1

            if skipstack == 0:
                skipinside = false
                skipstack = 1

        code_cursor += 1

    return "".join(["1" if x else "0" for x in result])


def main() -> None:
    try:
        print(zerone_exec(input("# ")))
    except KeyboardInterrupt:
        print()

