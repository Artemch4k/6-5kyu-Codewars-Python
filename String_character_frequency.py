def solve(s):
    check = []
    k = 0
    for x in s:
        check.append(str(s).replace(x,'',1))
    
    for x in check:
        a = [list(x).count(l) for l in list(x)]
        if len(set(a))==1: k = 1

    return True == k
