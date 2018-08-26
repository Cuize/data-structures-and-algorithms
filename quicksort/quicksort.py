from random import randint as rint
from dutch import dutch
def quicksort(nums):
    st=0
    ed=len(nums)-1
    if st>=ed:
        return
    stack=[(st,ed)]
    while stack:
        st,ed=stack.pop()
        j=rint(st,ed)
        flag=nums[j]
        i,n=dutch(nums,flag,st,ed)
        if i>st+1:
            stack.append((st,i-1))
        if n+1<ed:
            stack.append((n+1,ed))