from itertools import permutations

s = input("String")
permutation =   ["".join(p) for p in permutations(s)]
print(*permutation)