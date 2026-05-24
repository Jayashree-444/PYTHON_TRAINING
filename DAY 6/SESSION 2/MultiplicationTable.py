r=int(input("enter number of rows: "))
c=int(input("enter number of columns:" ))
r=[]
c=[]
sum=[]
num=0
for num in range(0,11):
    for num in range(0,10):
        sum.append(num)
    
    print(r*num,"x",num,"=",sum)
    print(c*num,"x",num,"=",sum)