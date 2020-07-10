'''
.count
.format
.isdigit
.islower
.isupper
.lower
.upper
.join
.replace
.split
.startswith
.endswith
.strip
'''
s1 = 'www.51reboot.com'
print(s1.count('www'))
s2 = '10011'
print(s2.isdigit())
s3 = 'ABCDd'
print(s3.islower())
print(s3.isupper())
print(s3.lower())
print(s3.upper())
print(s3.replace('CD', 'e'))

print(s1.startswith('w'))
# print(s1.endswith('com'))

s4 = ' www.51reboot. com '
print(s4.strip())
print(s4.lstrip())
print(s4.rstrip())
print()s4.