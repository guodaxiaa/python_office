m=10
a=[]
for i in range(1,m):
    for x in range(1,m):
        if x<=i:
            print(str(x),'*',str(i),'=',i*x,'\t',end=' ')

    print('')

