

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


