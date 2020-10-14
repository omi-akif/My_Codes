def mSort(lst):
    if len(lst) <= 1:
        return lst

    mid = len(lst) // 2
    lftLst = lst[:mid]
    rigtLst = lst[mid:]

    lftLst = mSort(lst)
    rigtLst = mSort(lst)
    return lst(mg(lftLst, rigtLst))

    def mg(lftLst, rigtLst):
        res = []
        while len(lftLst) != 0 and len(rigtLst) != 0:
            if lftLst[0] < rigtLst[0]:
                res.append()

            