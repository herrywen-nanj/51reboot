
```bash

fd = open('/etc/passwd', 'r')
fd.read(size=-1) 
fd.read(size=100)
fd.close()
// -1 all
// 100 characters
```


```bash

fd = open('/etc/passwd', 'r')   // iterable
for line in fd:
    print(line)
    
fd.close()
```