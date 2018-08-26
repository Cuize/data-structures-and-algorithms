nums=input("input nums with . to separate")
try:
	nums=[int(x) for x in nums.split(".")]
except:
	nums=nums.split(".")
print(f"your input is {nums}")
print("*"*10)
choice=input("find kth smallest element or simply sort the array?  (enter 0 for kth smallest element 1 for sorting)")
while choice not in "01":
	choice=input("find kth smallest element or simply sort the array?  (enter 0 for kth smallest element 1 for sorting)")

if choice=="1":
	print("Now run quicksort")
	from quicksort import quicksort
	quicksort(nums)
	print("*"*10)
	print("\n")
	print(f"sorted nums: {nums}")
else:
	print("Now find the kth smallest element")
	print("\n")
	k=int(input("please input the value of k"))
	from findkthsmall import findkthsmall
	ans=findkthsmall(nums,k)
	if k==1:
	    print("*"*10)
	    print("\n")
	    print(f"the smallest element of {nums} is {ans}")
	    print("\n")
	    print("*"*10)
	elif k==2:
	    print("*"*10)
	    print("\n")
	    print(f"the 2nd smallest element of {nums} is {ans}")
	    print("\n")
	    print("*"*10)
	elif k==3:
	    print("*"*10)
	    print("\n")
	    print(f"the 3rd smallest element of {nums} is {ans}")
	    print("\n")
	    print("*"*10)
	else:
	    print("*"*10)
	    print("\n")
	    print(f"the {k}th smallest element of {nums} is {ans}")
	    print("\n")
	    print("*"*10)





