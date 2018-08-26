from random import randint as rint
from dutch import dutch
def findkthsmall(nums,k):
    if not nums:
        return
    if k<1:
        k=1
    if k>len(nums):
        k=len(nums)
    stack=[(0,len(nums)-1,k)]
    while stack:
        st,ed,idx=stack.pop()
        j=rint(st,ed)
        piv=nums[j]
        i,n=dutch(nums,piv,st,ed)
        # <=piv: n-st+1, #<piv: i-st
        if i-st<idx<=n-st+1:
            return piv
        elif idx<=i-st:
            stack.append((st,i-1,idx))
        else:
            stack.append((n+1,ed,idx-n+st-1))