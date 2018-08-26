import bisect
class SegmentTree:
    def __init__(self,nums):
        self.len=len(nums)
        self.tree=[] # segment tree using array
        self.map={} # idx in nums to idx in tree
        stack=[[0,0,len(nums)-1]]
        length=0
        while stack:
            n,l,r=stack.pop()
            length=max(length,n)
            if l==r:
                self.map[l]=n
            elif l<r:
                stack.append([2*n+1,l,(l+r)//2])
                stack.append([2*n+2,(l+r)//2+1,r])
        self.tree=[float("inf")]*(length+1)
        for i,num in enumerate(nums):
            self.tree[self.map[i]]=num
        j=len(self.tree)-1
        while j>0:
            self.tree[(j-1)//2]=min(self.tree[j],self.tree[j-1])
            j-=2
            
    def mutate(self,idx,num):
        tidx1=self.map[idx]
        self.tree[tidx1]=num
        if tidx1%2:
            tidx2=tidx1+1
        else:
            tidx2=tidx1-1
        while 0<tidx1<len(self.tree) and 0<tidx2<len(self.tree) and self.tree[(tidx1-1)//2]>min(self.tree[tidx1],self.tree[tidx2]):
            tidx1=(tidx1-1)//2
            self.tree[tidx1]=num
            if tidx1%2:
                tidx2=tidx1+1
            else:
                tidx2=tidx1-1
    
    def rangeq(self,st,ed):
        ans=float("inf")
        stack=[[0,0,self.len-1]]
        while stack:
            n,l,r=stack.pop()
            if st<=l and ed>=r: # query cover the interval
                ans=min(ans,self.tree[n])
            elif r<st or ed<l: # no intersection
                continue
            else:
                stack.append([2*n+1,l,(l+r)//2])
                stack.append([2*n+2,(l+r)//2+1,r])
        return ans
if __name__ == '__main__':
    print("Implement the SegmentTree data structure")
    print("\n")
    nums=[int(x) for x in input("type in array of integers with . to separate").split(".")]
    tmp=SegmentTree(nums)
    while True:
        choice="x"
        print(f"your input nums now is {nums}")
        while choice not in "mrq":
            choice=input("want mutate, range_query or quit? type in m,r,or q")
        if choice=="m":
            idx,num=input("type in the index followed by value, separate by ',' ").split(",")
            idx=int(idx)
            num=int(num)
            nums[idx]=num
            tmp.mutate(idx,num)
        elif choice=="r":
            st,ed=input("type in the left index followed by right index, separate by ',' ").split(",")
            st=int(st)
            ed=int(ed)
            ans=tmp.rangeq(st,ed)
            print("*"*15)
            print("\n")
            print(f" the minimum value for nums from index {st} to {ed} (which is {nums[st:ed+1]}) is {ans}")
        else:
            break
    
