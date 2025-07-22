'''
394. 字符串解码

'''

s = "3[a]2[bc]"
def decodeString(s):
    stack = []
    res = ""
    num = 0

    for c in s:
        if c == '[':
            stack.append((res, num))
            res = ""
            num = 0
        elif c == ']':
            tmp = stack.pop()
            res = tmp[0] + tmp[1] * res
        elif c.isdigit():
            num = num*10 + int(c)
        else:
            res += c
    return res


print(decodeString(s))


