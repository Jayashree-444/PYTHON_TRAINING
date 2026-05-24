class TreeNode:
    def __init__(self,val=0):
        self.val=val
        self.left=None
        self.right=None
        # level-Ordered Insertion
class Solution:
    # depth 1st search
    def rob(self,root):
        def dfs(node):
            if not node:
                return [0,0]
            # left
        left=dfs(node.left)
        # right
        right=dfs(node.right)
        
        # robb values
        rob_values=node.val+left[1]+right[1]
        
        # not robb
        not_rob=max(left)+max(right)
        
        return max(dfs(root))
    
      # level-Ordered Insertion
    def buildTree(arr):
        if not arr or arr[0] is None:
            return None
        root=TreeNode(arr[0])
        queue=[root]
        i=1
        while queue and i<len(arr):
            current=queue.pop(0)
            # left child
            if i<len(arr) and arr[i] is not None:
                current.left=TreeNode(arr[i])
                queue.append(current.left)
            i+=1
            if i<len(arr) and arr[i] is not None:
                current.right=TreeNode(arr[i])
                queue.append(current.right)
            i+=1
            
            
        return root  
Sample=[[3,2,3,None,3,None,1],
        [3,4,5,1,3,None,1],
        [5],
        [1,2,3],
        [4,1,None,2,None,3]]
  # 3
#2   #3
  #3   #1
obj=Solution()
root=obj.buildTree(Sample)
print("max: ",obj.rob(root))
      

    
    