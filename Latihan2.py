max = 0
while True:
    a = int(input("Masukan bilangan = "))
    if max < a:
        max = a
    if a==0:
        break
print("Bilangan Terbesar adalah",max)
