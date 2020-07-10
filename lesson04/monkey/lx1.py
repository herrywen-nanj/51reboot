

# sum
'''
i = 1
ssum = 0

while i <= 100:
    # print(i)
    ssum += i
    i += 1

print(ssum)
'''

'''
i = 1
arr = []

while i <= 100:
    # print(i)
    arr.append(i)
    i += 1

print(arr)
print(sum(arr))
'''


'''
In [1]: range?                                                                                                                                               
Init signature: range(self, /, *args, **kwargs)
Docstring:     
range(stop) -> range object
range(start, stop[, step]) -> range object

Return an object that produces a sequence of integers from start (inclusive)
to stop (exclusive) by step.  range(i, j) produces i, i+1, i+2, ..., j-1.
start defaults to 0, and stop is omitted!  range(4) produces 0, 1, 2, 3.
These are exactly the valid indices for a list of 4 elements.
When step is given, it specifies the increment (or decrement).
'''

'''
print(sum(list(range(1, 101))))
print("-"*100)

print(list(range(0, 101, 2)))
print(len(list(range(0, 101, 2))))
print(sum(list(range(0, 101, 2))))
print("-"*100)

print(list(range(1, 101, 2)))
print(len(list(range(1, 101, 2))))
print(sum(list(range(1, 101, 2))))
'''
'''
idx = 0
arrlist = ['a', 'b', 'c', 'c', 'a', 'd', 'e']

for i in arrlist:
    print(idx, i)
    idx += 1
'''
arrlist = ['a', 'b', 'c', 'c', 'a', 'd', 'e']
for vinfo in enumerate(arrlist):
    print(vinfo[0], vinfo[1])


for idx, v in enumerate(arrlist):
    print(idx, v)





