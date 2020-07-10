

'''
open(
    file,
    mode='r',
    buffering=-1,
    encoding=None,
    errors=None,
    newline=None,
    closefd=True,
    opener=None,
)
'''

import json

# 1. 打开文件 file describe
fd = open("51reboot.txt", 'r')


# 2. 操作文件 read / write
data = fd.read()
# print(type(data))
membuf = json.loads(data)
print(membuf, type(membuf))

# 3. 关闭文件
fd.close()