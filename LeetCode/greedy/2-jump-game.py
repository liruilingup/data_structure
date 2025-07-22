'''
示例 1：

输入：nums = [2,3,1,1,4]
输出：true
解释：可以先跳 1 步，从下标 0 到达下标 1, 然后再从下标 1 跳 3 步到达最后一个下标。
'''

def canJump(nums):
    if nums == [0]: return True
    max_jump = 0
    end_jump = len(nums)-1
    for k, v in enumerate(nums):
        if max_jump>=k and k+v>max_jump: # 如果当前位置能到达，并且当前位置+跳数>最远位置  
            max_jump = k+v
            if max_jump>=end_jump:
                return True
    return False



print(canJump(nums = [2,3,1,1,4]))