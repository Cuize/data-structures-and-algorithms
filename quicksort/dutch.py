
def dutch(nums,flag=0,st=0,ed=1):
    """
    dutch function partially order the input nums in-place 
    according to the order: <flag =flag >flag
    for details see 'dutch flag algorithm'
    inputs:
        nums: list[int]
        flag: int
        st: int
        ed: int
    output: list[int]
    default:
        flag=0
        st=0
        ed=len(nums)-1
    """
    
    
    i=st
    j=st
    n=ed
    while j<=n:
        if nums[j]<flag:
            if i==j:
                pass
            else:
                nums[i],nums[j]=nums[j],nums[i]
            i+=1
            j+=1
        elif nums[j]>flag:
            nums[j],nums[n]=nums[n],nums[j]
            n-=1
        else:
            j+=1
    return i,n