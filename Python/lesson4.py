def bSort(lst):
    for iNum in range(len(lst)-1,0,-1):
        for iDx in range(iNum):
            if lst[iDx]>lst[iDx+1]:
                lst[iDx], lst[iDx+1] = lst[iDx+1], lst[iDx]
                
                print(lst)


lst=[3,7,2,9,2,6,5,1]
bSort(lst)
print('\n')
print(lst)