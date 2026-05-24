rows=4
#upper part
for i in range(1,rows+1):
    #right anngled triangle
    for j in range(i):
          print("*",end=" ")
          # spaces in middle
          for j in range(2*(rows-i)):
           print("*",end=" ")
# mirror of right angled triangle
for i in range(i):
    print("*",end=" ")
    print( )
#upper part
for i in range(rows,0,-1):
#right anngled triangle
    for j in range(i):
          print("*",end=" ")
          # spaces in middle
          for j in range(2*(rows-i)):
             print("*",end=" ")
             # mirror of right angled triangle
             for i in range(i):
                 print("*",end=" ")
          print( )