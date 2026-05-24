def is_valid(s):
    stack=[]
    map={')':'(',
         '}':'{',
         ']':'['}
    
    for ch in s:
        if ch in map: # is that closing bracket in map or in not
            top=stack.pop() if stack else '#' # is placeholder if stack is empty always store placeholder hash(#)
            if map[ch]!=top:
                return False
            else:
                stack.append(ch)
    return not stack

print(is_valid("()[]{}"))
            