'''
列表的排序
'''
intervals = [[1,3],[2,6],[8,10],[15,18]]
intervals = [[1,4],[0,4]]
# intervals =[[1,4],[2,3]]

def merge(intervals):
    """
    56. 合并区间
    """
    nums_sorted = sorted(intervals, key=lambda x:x[0])
    res = [nums_sorted[0]]
    for i in range(1, len(nums_sorted)):

        if res[-1][1] > nums_sorted[i][0]:
            res[-1] = [res[-1][0], max(nums_sorted[i][1], res[-1][1])]
        else:
            res.append(nums_sorted[i])

    return res


print(merge(intervals))


