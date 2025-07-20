''' 滑动窗口'''

s = "cbaebabacd"
p = "abc"

out_put = [0,6]


def findAnagrams(s, p):
    """
    438. 找到字符串中所有字母异位词
    """
    result = []
    strs = list(s)
    m = len(s)
    n = len(p)
    demo = "".join(sorted(list(p)))
    print(demo)
    for key in range(0, m-n+1):
        tmp = "".join(sorted(strs[key:key+n]))
        if tmp == demo:
            result.append(key)

    return result

print(findAnagrams(s, p))




