"""
给你一个字符串 s，找到 s 中最长的 回文 子串。


"""
s = "babad"

def longestPalindrome(s):
    res = ''
    for i in range(len(s)):
        start = max(i - len(res) -1, 0)
        temp = s[start: i+1]
        if temp == temp[::-1]:
            res = temp
        else:
            temp = temp[1:]
            if temp == temp[::-1]:
                res = temp
    return res


print(longestPalindrome(s))
