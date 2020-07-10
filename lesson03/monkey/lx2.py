"""
>乘法口诀
```
1. * =  (format)
2. 5个元素 (format)
3. 1 * n（line） range
4. for 2层
```
"""


for i in range(1, 10):
    for j in range(1, i + 1):
        # print(i, j)
        print("{} * {} = {}".format(j, i, i * j), end=" ")
    input()
