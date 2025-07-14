strs = ["eat", "tea", "tan", "ate", "nat", "bat"]

out = [["bat"],["nat","tan"],["ate","eat","tea"]]

def groupAnagrams(strs):
	"""
	49. 字母异位词分组
	"""
	print("---")

	for str in strs:
		print(sorted(list(str)))


groupAnagrams(strs)

