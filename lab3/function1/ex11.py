def pal(s):
    l = len(s)
    ns = ""
    for i in range(l):
        ns += s[l-i-1]
    if ns == s:
        return True
    else:
        return False



print(pal("ma"))