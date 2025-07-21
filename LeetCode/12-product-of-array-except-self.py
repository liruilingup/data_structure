nums = [1,2,3,4]

def productExceptSelf(nums):
    n = len(nums)

    rs_l, rs_r = [1] * n, [1] * n

    # 前缀积
    for i in range(1, n):
        rs_l[i] = rs_l[i-1] * nums[i-1]

    # 后缀积
    for i in range(n-2, -1, -1):
        rs_r[i] = rs_r[i+1] * nums[i+1]

    # 乘在一起
    for i in range(n):
        rs_l[i] *= rs_r[i]

    return rs_l

print(productExceptSelf(nums))


