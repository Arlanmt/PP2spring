def rev():
    s = input("Give a string: ")
    s = s.split()
    l = len(s)
    new_s = ""
    for i in range(l):
        new_s +=s[l-i-1]
        new_s += " "
    print(new_s)
        
rev()