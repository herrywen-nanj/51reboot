#Filename : 9x9.py
#author by: Thomas.Wu
#use for
print("------------------Use  for to do 9x9----------------")
for i in range(1, 10):
    for j in range(1, i+1):
        print('{}x{}={}\t'.format(j, i, i*j), end='')
    print()
#V2
#use  while
print("------------------Use While to 9x9------------------")
i = 1
while i <= 9:
       j = 1
       while j <= i:
          print('{}x{}={}\t'.format(i,j,i*j),end='')
          j= 1+j
       i=i+1
       print()
