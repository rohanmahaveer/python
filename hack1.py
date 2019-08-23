r=4
c=7
for i in range(r):
    for j in range(c):
        if((i==0 and j%3==0) or (i==1 and j%3==0) or (i==2 and j%2==0)or(i==2 and j%3==0) or (i==3 and j%2!=0 and j%3!=0)):
              print('*', end="")
        else:
            print(end=" ")


    print()
for i in range(r):
    for j in range(c):
        if((i==0 or i==3) or (i==1 and j%6==0)or (i==2 and j%6==0)):
              print('*',end="")
        else:
             print(end=" ")


    print()
for i in range(r):
    for j in range(c):
        if((i==0 and j%3==0) or (i==1 and j%3==0) or (i==2 and j%2==0)or(i==2 and j%3==0) or (i==3 and j%2!=0 and j%3!=0)):
              print('*',end="")
        else:
             print(end=" ")


    print()
