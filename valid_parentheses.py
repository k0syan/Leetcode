s = "]"
par = list(s)
stack = []
i = 0
correct = True
while i < len(par):
    p = par[i]
    if p == "(" or p == "{" or p == "[":
        stack.append(p)
    else:
        if len(stack) == 0:
            correct = False
            break
        if p == ")":
            if stack[len(stack) - 1] == "(":
                stack.pop()
            else:
                correct = False
                break
        elif p == "}":
            if stack[len(stack) - 1] == "{":
                stack.pop()
            else:
                correct = False
                break
        elif p == "]":
            if stack[len(stack) - 1] == "[":
                stack.pop()
            else:
                correct = False
                break
    i += 1
if len(stack) != 0:
    correct = False
print(correct)
