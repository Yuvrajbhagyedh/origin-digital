nums = [3, 2, 4]
target = 6

dict1={}

for i in range(len(nums)):
    num=nums[i]
    comp=target-num

    if comp in dict1:
        print((dict1[comp],i))
        break
    dict1[num]=i