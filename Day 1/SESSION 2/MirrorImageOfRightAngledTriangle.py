rows=4
for i in range(1,rows+1):
    # print spaces first
    for j in range(rows-i):
        print(" ",end=" ")
    # starts
    for j in range(i):
        print("*",end=" ")
    print()