
'''
fd = open('/etc/passwd', 'r')

data = fd.read()
print(data)

fd.close()
'''

with open('/etc/passwd', 'r') as fd:
    data = fd.read()
    print(data)


print("Read end.")