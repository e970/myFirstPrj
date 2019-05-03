import random
r=[]
d=10
dd=d*d
r=random.sample(range(1,dd+1),dd)
#print(r,sum(r),end='\n\n')
for i in range(1,dd+1):
    print('%4d'%r[i-1],end='')
    if i % d == 0:
       print ()
#HELLO 1
