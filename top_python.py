# 生成列表
i = 10
print([1] * i)
print([0 for k in range(i)])


# 求取绝对值的函数
print(abs(1-2))

# 求和
a = [1,2,4]
print(sum(a))


# 求前缀和
nums = [1,-1,0]
# 方法1
sum_nums = [0]
for i in nums:
    sum_nums.append(sum_nums[-1] + i)
print(sum_nums)
# 方法2
s = [0] * (len(nums) + 1)
for i, x in enumerate(nums):
    s[i + 1] = s[i] + x
print(s)
