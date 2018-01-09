n=int(input('请输入一个整数'))
s=0
jc=1
a=[]
for i in range(1,(n+1)):
    a.append(i)
m=len(a)
while i <=m:
    for x in range(m):
        jc=jc*a[x]
        s=s+jc
    m=m-1

print(s)

