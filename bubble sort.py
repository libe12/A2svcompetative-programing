def countSwaps(a):
    total_count=0
    for i in range(0,len(a)-1):
        nums_count=0
        for j in range(len(a)-1):
            if a[j]>a[j+1]:
               a[j],a[j+1]=a[j+1],a[j]
               nums_count+=1
               total_count+=1
        if nums_count==0:
            break
    print ("Array is sorted in {} swaps.".format(total_count))
    print ("First Element: {} " .format(a[0]))
    print ("Last Element: {} " .format(a[-1]))
