def kopaytma(sonlar) :
    kopaytma =1

    for son in sonlar:
        kopaytma *= son

    return kopaytma
    

print(kopaytma([1,2,3,4]))