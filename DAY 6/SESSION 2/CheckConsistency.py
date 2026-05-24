def countConsistency(allowed,words):
    allowed_set=set(allowed)
    
    for word in words:
        consistent=True
        
        for ch in word:
            if ch not in allowed_set:
                consistent=False
                break
            if consistent:
                count+=1
                
        return count
    
# main
allowedString="ab"
words=["ad","bd","aaab","badab"]
print(countConsistency(words))