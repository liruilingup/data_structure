s = "abcabcbb"
output = 3

def lengthOfLongestSubstring(s):
    """
    3. 无重复字符的最长子串
    """
    sub_str = ""
    strs = list(s)
    res = 0

    for i in range(len(strs)):
        left = strs[i]
        for j in range(i, len(strs)):
            if (j+1-i) == len(set(strs[i:j+1])):
                # print( strs[i:j+1])
                res = max(res, j+1-i)
                continue
            else:
                break
    return res
print(lengthOfLongestSubstring(s))

