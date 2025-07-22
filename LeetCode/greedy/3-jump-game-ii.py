
nums = [2,3,1,1,4]

def jump(nums):
    jumps = mx = last = 0
    for i, x in enumerate(nums[:-1]):
        mx = max(mx, i + x)
        if last == i:
            jumps += 1
            last = mx
    return jumps


print(jump(nums))

