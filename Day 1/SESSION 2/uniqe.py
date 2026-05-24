def single_Number(nums):
    xor=0
    for num in nums:
        xor=xor^num
        diff_bit=xor &-xor
        a=0 #1st bucket
        b=0 #2nd bucket
        for num in nums:
            if(num&diff_bit)==0:
                a=a^num
            else:
                b=b^num
        return[a,b]
# main
num=set()
nums=[1,2,1,2,4,5]
result=single_Number(nums)
print(result[0],result[1])
