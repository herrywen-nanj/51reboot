

import os
#
# result = os.system("dxxf") # os.stdout > 2
# # print("---------------------")
# # print('result: {}'.format(result))
# print(result)

import shlex
import subprocess

cmd = 'dfxxxxx -h'
# cmd = shlex.split(cmd)
# print(cmd)

p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
stdout, stderr = p.communicate()

if stderr:
    print(stderr)
    print("Exec fail")
else:
    print(stdout)
    print("Exec succ")



