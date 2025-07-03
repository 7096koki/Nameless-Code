def Befunge(code):
    x = 0
    y = 0
    dire =  None
    str_check = False
    stack = []
    while True:
        a = code[y][x]
        if a in ["^", "v", ">", "<"]:
            dire = a
        elif a == "\"":
            str_check = not str_check
        elif a == ",":
            print("".join(stack))
        elif a == "@":
            break
        else:
            if str_check != True:
                print(f'"{a}"is not defined.')
            else:
                stack.append(a)
        

        if dire == "^":
            y -= 1
        elif dire == "v":
            y += 1
        elif dire == ">":
            x += 1
        elif dire == "<":
            x -= 1

        if len(code[y]) == x:
            break

test = [[">", '"', "H", "e", "l", "l", "o", '"', "v", " ", " ", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " ", ">", '"', "W", "o", "r", "l", "d", "!", '"', ","]]
Befunge(test)
