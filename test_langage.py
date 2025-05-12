def test(code):
    accumlator = 0
    stack = []
    for i in code:
        if i == "+":
            accumlator += 1
        elif i == "*":
            accumlator *= 2
        elif i == "-":
            accumlator -= 1
        elif i == "/":
            if accumlator != 0:
                accumlator //= 2
        elif i == "a":
            stack.append(chr(accumlator))
        elif i == "s":
            stack.append(str(accumlator))
        elif i == "c":
            accumlator = 0
        elif i == "p":
            print("".join(stack))
            stack = []

test("+******++++++++ac+*******---------------------------a+++++++aa+++ac+*****a+****+++++++++++++++++++++++ac+*******-----------------a+++a------a--------ac+*****+ap")
