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


def longestPalindrome2(s):
    length = len(s)
    dp = [[1] * length for _ in range(length)]

    left, right = 0, 0  # 长度为1时
    # 斜着遍历二维数组的上半部分
    for i in range(1, length):
        for j in range(length - i):
            if s[j] == s[j + i] and dp[j + 1][j + i - 1]:
                dp[j][j + i] = 1
                left, right = j, j + i
            else:
                dp[j][j+i] = 0
    return s[left: right + 1]


print(longestPalindrome2(s))

