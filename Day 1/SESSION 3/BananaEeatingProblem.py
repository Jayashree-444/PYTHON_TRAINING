piles=[3,6,7,11]
h=8
left=1
right=max(piles)
answer=right#11
#algorithm
while left<=right:
    mid=(left+right)//2
    total_hours=0
    for pile in piles:
        total_hours+=(pile+mid-1)//mid
        if total_hours<=h:
            answer=mid
            right=mid-1
        else:
            left=mid+1
print(answer)