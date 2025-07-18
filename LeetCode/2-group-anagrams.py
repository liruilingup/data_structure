strs = ["eat", "tea", "tan", "ate", "nat", "bat"]

out = [["bat"],["nat","tan"],["ate","eat","tea"]]

def groupAnagrams(strs):
    """
    49. 字母异位词分组
    """
    res_dict = {}
    for str in strs:
        tmp = "".join(sorted(list(str)))
        if tmp in res_dict:
            res_dict[tmp].append(str)
        else:
            res_dict[tmp] = [str]
    
    result = []
    for key, value in res_dict.items():
        result.append(value)
    return result

print(groupAnagrams(strs))

