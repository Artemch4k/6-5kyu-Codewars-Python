def count_feelings(st, arr):
    check = []
    if len(arr) == 0: return '0 feelings.'
    
    if len(st) >= len(max(arr)):
        saint = ' '.join(arr)
        for x in st:
            if x in saint:
                saint = saint.replace(x,'1')

        check = [x for x in saint.split() if x.count('1') == len(x)]       
    if len(check) == 1: return f"{len(check)} feeling."
    else: return f"{len(check)} feelings."