FILENAME = '/etc/passwd'

with open(FILENAME) as fd:
    for line in fd:
        lineArr = line.strip('\n').split(':')
        print(lineArr)
        # print("{} {} {} {}".format(lineArr[0], lineArr[2], lineArr[5], lineArr[6]))
        #print("{:<10}|{:^5} {:>30} {:>30}".format(lineArr[0], lineArr[2], lineArr[5], lineArr[6])
      #  print("{:<10}|{:^5} {:>30} {:>30}".format(lineArr[0], lineArr[2], lineArr[5], lineArr[6]))

