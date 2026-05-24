def baseBallGame(games):
    stack=[]
    for game in games:
        
        if game=="+":
            sum=stack[-1]+stack[-2] 
            stack.append(sum)
        elif game=="D":
            sum=2*stack[-1]
            stack.append(sum)
        elif game=="C":
            stack.pop()
        else:
            stack.append(int(game))
            
            return sum(stack)
    
gameList=["5","2","C","D","+"]
result = baseBallGame(games)
print("Total Score:", result)

    