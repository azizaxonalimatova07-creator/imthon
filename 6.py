def qiymatlar_yigindisi(lugat) :
    natija = 0 

    for kalit in lugat: 
        natija += lugat[kalit]
    return natija

print(qiymatlar_yigindisi({"a": 1, "b": 2, "c": 3}))