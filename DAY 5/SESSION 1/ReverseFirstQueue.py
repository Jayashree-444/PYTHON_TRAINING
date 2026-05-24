from collections import deque

def reverse(queue,k):
    if not queue or k>len(queue) or k<0:
        return  False

    stack=[]
    for i in range(k):
        stack.append(queue.popleft()) # adds 1st queue value and in py there is no deque delete option so we use popleft 
    while stack:
        queue.append(stack.pop())
    for i in range(len(queue)-k): # queue(n) n=5 k=3 so  n-k=2 (5-3=2)
        queue.append(queue.popleft()) # self adding to queue the poped element
    return queue
# main
queue=deque([1,2,3,4,5])
print(reverse(queue,3))