def Ticekt_Price(a,j,c,d):
    if c<=60:
        Price=10
    else:
        if d%2==0:
            if a<=d//2:
                Price=10
            else:
                Price=8
        else:
            if a<=d//2:
                Price=10
            else:
                Price=8
    return Price
