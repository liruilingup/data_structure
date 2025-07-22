
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

