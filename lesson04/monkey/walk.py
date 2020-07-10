
import os
import time

for dirpath, dirnames, filename in os.walk('/usr/local'):
    print(dirpath, dirnames, filename)
    print("--------")
    # time.sleep(1)