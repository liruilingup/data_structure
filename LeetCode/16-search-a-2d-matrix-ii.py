
'''
编写一个高效的算法来搜索 m x n 矩阵 matrix 中的一个目标值 target 。该矩阵具有以下特性：

每行的元素从左到右升序排列。
每列的元素从上到下升序排列。
'''

matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
target = 5
def searchMatrix(matrix, target):
    """
    240. 搜索二维矩阵 II
    """
    for row in matrix:
        if target < row[0]:
            return False
        if target > row[-1]:
            continue
        if row[0] <= target <= row[-1]:
            if target in row:
                return True
    return False


print(searchMatrix(matrix, target))


