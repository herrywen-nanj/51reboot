#!/bin/env python3

import pexpect

def ssh_command(user,host,password,command):
    ssh_newkey="Are you sure you want to continue connecting"

    # 为ssh生成一个spawn
    child = pexpect.spawn("ssh -l {} {} {}".format(user,host,command))

    # 如果登陆超时，打印错误信息
    try:
        child.send("yes")
        child.expect([pexpect.TIMEOUT, ssh_newkey, "password: "])
    except Exception as e:
        print("Ssh could not login,")
        return  "SSH could not login", False
    else:
        child.sendline(password)
        child.expect(pexpect.EOF)
        print(child.before)
    finally:
        return "Ssh success",True



ssh_command("root","192.168.64.128","docker","ls -l")