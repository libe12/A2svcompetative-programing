def countingValleys(steps, path):
    c=0
    r=0
    for i in path:
        if i=='U':
            c+=1
        else:
            c-=1
        if c==0 and i=='U':
            r+=1
    return r
