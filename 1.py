def musbat_yigindi(sonlar) :
    yigindi   = 0

    for son in  sonlar:
        if son > 0:
            yigindi += son
    return yigindi

print(musbat_yigindi([1, -2, 3,-4, 5]))

