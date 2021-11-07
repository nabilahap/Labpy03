a = 100000000
for x in range(1, 9):
    if(x >= 1 and x <= 2):
        b = a*0
        print("Laba bulan ke-",x," : ",b)
    if(x >= 3 and x <= 4):
        c = a*0.1
        print("Laba bulan ke-",x," : ",c)
    if(x >= 5 and x <= 7):
        d = a*0.5
        print("Laba bulan ke-",x," : ",d)
    if(x == 8):
        e = a*0.3
        print("Laba bulan ke-",x," : ",e)
total = b+b+c+c+d+d+e
print("\Total : ",total)
