def has_33(nums):
    l = len(nums)
    k = 0
    for i in nums:
        num = i
        print(num)
        if num == 3 and k == 3:
            return True
            break
        else:
            k = 0
        
        if num == 3:
            k = 3
            continue
    
        

    
print(has_33([3,3,3,3]))