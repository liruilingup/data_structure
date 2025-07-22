temperatures = [73,74,75,71,69,72,76,73]


def dailyTemperatures(temperatures):
        
    res = [0] * len(temperatures)
    stack = []

    for i in range(len(temperatures)):
        while stack and temperatures[i] > temperatures[stack[-1]]:
            index = stack.pop()
            res[index] = i - index
        stack.append(i)
    return res 

print(dailyTemperatures(temperatures))


