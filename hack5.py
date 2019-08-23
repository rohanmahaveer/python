num=int(input("enter any 3 digit number"))
n1=num
rev=0
res=0
sum=0
while(n1>0):
  rem=n1%10
  rev=(rev*10)+rem
  n1=n1//10
print("reverse of entered number is:",rev)
n2=rev
if(num>n2):
    res=num-n2
else:
    res=n2-num
print("sub value is :",res)
rev1=0
n3=res
while(n3>0):
    rem1=n3%10
    rev1=(rev1*10)+rem1
    n3=n3//10
print("reverse of subtracted number:",rev1)
sum=res+rev1
print("wow factor is: ",sum)
