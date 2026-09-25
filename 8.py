def absolyutlar(sonlar) :
    natija = []

    for son in sonlar:
        if son < 0:
            natija.append(-son)
        else:
            natija.append(son)
    return natija
    

print(absolyutlar([-3, 2, -1]))