name=input("enter ur name: ")
mid=len(name)//2
fh=name[ :mid] #first half
sh=name[mid: ] #second half
fhRev=fh[::-1]
shRev=sh[::-1]
result=fhRev+shRev
print("output: ",result)

