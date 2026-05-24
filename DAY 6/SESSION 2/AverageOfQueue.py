from queue import Queue

def avg(q):
    total=0
    n=q.qsize()
    temp=Queue()
  
   # sum
    while not q.empty():
        value=q.get()
        total+=value
        temp.put(value)
    while not temp.empty():
        q.put(temp.get())
        
    return total/n 


       
      # input  
n=int(input("enter the size of queue: "))
q=Queue()

print("enter the elements: ")
elements=list(map(int,input().split()))

for i in range(n):
    q.put(elements[i])
avg=avg(q)
print("Average of elements: ",avg)
    
      

