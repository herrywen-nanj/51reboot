

def fditer():

    with open('/etc/passwd', 'r') as fd:
        for line in fd:
            yield line


for i in dir(fditer):
    print(i)