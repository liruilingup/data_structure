'''
20. 有效的括号
'''


s = "()"
def isValid(s):
    dicts = {")":"(", "}":"{", "]":"["}
    stack = []
    for c in s:
        if stack and c in dicts:
            if stack.pop() == dicts[c]: # 可以配对
                continue
            else:
                return False

        else:
            stack.append(c)
    return stack == []
print(isValid(s))


