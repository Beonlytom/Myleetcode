def isValid(s):
    stack = []
    for i in s:
        if i == "(" or i =="[" or i =="{":
            stack.append(i)
        if i == ")" or i =="]" or i =="}":
            print("cazzo" + i)
            if stack == []:
                return False
            if i == ")":
                if stack[-1] != "(":
                    return False
                stack.pop()
            if i == "]":
                if stack[-1] != "[":
                    return False
                stack.pop()
            if i == "}":
                if stack[-1] != "{":
                    return False
                stack.pop()
            print(stack)
    if stack == []:
        return True
    else:
        return False


print(isValid("(])"))