def clown(nums):
    nlist = []
    l = len(nums)
    for i in nums:
        if i in nlist:
            continue
        else:
            nlist.append(i)
    return nlist




print(clown([1,1,2,2,3,3]))