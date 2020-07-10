import psutil

# cpu

cpu_info = psutil.cpu_times()
print("cpu执行用户进程时间: {}".format(cpu_info.user))
print("cpu执行系统调用时间: {}".format(cpu_info.system))

mem_info = psutil.virtual_memory()

print(mem_info)
print("总内存:{}".format(mem_info.total))
print("可用内存:{}".format(mem_info.available))
print("内存使用率: {}".format(mem_info.percent))
print("swap内存: {}".format(psutil.swap_memory()))


# 硬盘
disk_info = psutil.disk_partitions()
print(disk_info)
G=1024*1024*1024
disk_mes = psutil.disk_usage("/")
print(disk_mes)
