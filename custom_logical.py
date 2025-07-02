def custom_logical(is_NOT, a, op, b):
    op = op.upper()
    is_NOT = is_NOT.upper()
    result = None
    if op == "AND":
        if (a, b) == (True, True):
            result = True
        else:
            result = False
    elif op == "OR":
        if True in (a, b):
            result = True
        else:
            result = False
    elif op == "XOR":
        if (a, b) == (True, False):
            result = True
        elif (a, b) == (False, True):
            result = True
        else:
            result = False

    if is_NOT == "NOT":
        if result == True:
            result = False
        else:
            result = True

    return result
    
print(custom_logical("NONE",False, "XOR", True))
