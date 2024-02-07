def spy_game(nums):
    nd = [0,0,7]
    sol = []
    ng =nd
    for i in nums:
        for j in nd:
            if i == j:
                sol.append(i)
                nd.remove(j)


    ng = [0,0,7]
    if sol == ng:
        return True
    else:
        return False
print(spy_game([1,7,2,0,4,5,0]))