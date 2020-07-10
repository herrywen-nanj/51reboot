import time
import threading


def aws_meiguo():
    print("aws meiguo")
    time.sleep(10)
    print("aws meiguo end")

def aws_china():
    print("aws china")
    time.sleep(5)


def ali_china():
    print("ali meiguo")
    time.sleep(3)
    print("部署服务成功，挂在流量到调度层, hook到对应的接口上。")

cur_time = time.time()
# aws_meiguo()
# aws_china()
# ali_china()


th1 = threading.Thread(target=aws_meiguo, name="aws meiguo")
th2 = threading.Thread(target=aws_china, name="aws china")
th3 = threading.Thread(target=ali_china, name="aws china")
threads = [th1, th2, th3]

for th in threads:
    th.setDaemon(False)
    th.start()

# print("join")
# for th in threads:
#     th.join()
# print("join end")


print(time.time()-cur_time)
print("End")

while True:
    time.sleep(1)