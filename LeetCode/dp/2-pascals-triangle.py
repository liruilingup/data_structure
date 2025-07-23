'''
给定一个非负整数 numRows，生成「杨辉三角」的前 numRows 行。

在「杨辉三角」中，每个数是它左上方和右上方的数的和。
示例 1:

输入: numRows = 5
输出: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
示例 2:

输入: numRows = 1
输出: [[1]]
'''

numRows = 5
def generate(numRows):
    if numRows==1:
        return [[1]]
    if numRows==2:
        return [[1], [1,1]]
    res=[[1], [1,1]]
    def dfs(i):
        # 3
        tmp = [1]
        for j in range(1, i-1):
            tmp.append(res[-1][j-1] + res[-1][j])
        tmp.append(1)

        res.append(tmp)

    for k in range(3, numRows+1):
        dfs(k)
    return res
        
print(generate(numRows))

