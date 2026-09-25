def raqamlar_son(matn) :
    soni = 0

    for belgi in matn:
        if not belgi.isdigit():
            soni +=1
    return soni
    
print(raqamlar_son("abc123"))