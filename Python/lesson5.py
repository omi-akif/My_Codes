def mSort(uLst):
    if len(uLst) <=1:
        return uLst
    divLst = len(uLst) // 2
    lftLst = uLst[:divLst]
    ritLst = uLst[divLst:]

    lftLst = mSort(lftLst)
    ritLst = mSort(ritLst)
    
    return uLst