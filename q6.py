import random

nums = []
result = 0
newResult = ''
idx = 1

for i in range(5):
    result = 0
    newResult = ''
    for i in range(6):
        result = str(random.randint(0, 9))
        newResult+=result
    nums.append(newResult)

for i in nums:
    print(idx, 'número', i)
    idx+=1