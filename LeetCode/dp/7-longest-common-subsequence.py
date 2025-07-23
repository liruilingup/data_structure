'''
1143. 最长公共子序列
'''

'''
给定两个字符串 text1 和 text2，返回这两个字符串的最长 公共子序列 的长度。如果不存在 公共子序列 ，返回 0 。

一个字符串的 子序列 是指这样一个新的字符串：它是由原字符串在不改变字符的相对顺序的情况下删除某些字符（也可以不删除任何字符）后组成的新字符串。

例如，"ace" 是 "abcde" 的子序列，但 "aec" 不是 "abcde" 的子序列。
两个字符串的 公共子序列 是这两个字符串所共同拥有的子序列。
'''

text1 = "abcde"
text2 = "ace" 

def longestCommonSubsequence(text1,text2):
    m, n = len(text1), len(text2)

    # 初始化
    dp = [0] * (n+1)

    # 状态更新
    for i in range(1, m+1):
        dp2 = [0] * (n+1)   # 滚动数组
        for j in range(1, n+1):
            if text1[i-1] == text2[j-1]:
                dp2[j] = dp[j-1] + 1
            else:
                dp2[j] = max(dp[j], dp2[j-1])
        dp = dp2            # 滚动数组
    
    return dp[n]


