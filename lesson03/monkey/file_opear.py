

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
fd = open("51reboot.txt", 'w')


# 2. 操作文件 read / write
try:
    datamsg = [
        ["monkey1", 12, 13987654321, "monkey@51reboot.com"],
        ["monkey2", 12, 13987654321, "monkey@51reboot.com"],
        ["monkey3", 12, 13987654321, "monkey@51reboot.com"],
    ]
    fd.write(json.dumps(datamsg))
except Exception as e:
    print("Write file error, errmsg: {}".format(e))
finally:
    fd.close()

#
# fd.write("1\n")
# fd.write("2\n")
# fd.write("3\n")
# fd.write("fsljflkajflajsflsadjflajfal\n")
#


# 3. 关闭文件
# fd.close()