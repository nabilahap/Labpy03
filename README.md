# Labpy03

### Profil
__Nama  : Nabilah Ananda Putri__

__Nim   : 312110263__

__Kelas : T1.21.A.1__

#### Daftar Isi
| No | ISI | 
| -- | --- |
| 1. | Latihan1  |
| 2. | Latihan2  |
| 3. | Praktikum2 |
## Lab 2

## Latihan1
1. Tampilakn n jumlah bilangan acak yang lebih kecil dari 0.5
2. Nilai n diisi pada saat runtime
3. Kalian bisa menggunakan kominasi while dan for untuk menyelesaikannya
4. Gunakan fungsi random() yang dapat diimport terlebih dahulu

#### Program dan Output

![Gambar1](ssP3/ssP3Lat1.png)

- Langkah-langkah
1. Masukan fungsi random terlebih dahulu
2. Deklarasi interger
3. Masukan deskripsi kombinasi for untuk menyelesaikannya
4. Masukan nilai jumlah (n) : 0.5
5. Mencetak data ke-1 sampai ke-5 hasil nilai kurang dari 0.5


```bash 
from random import random
n = int(input("Masukan Nilai N: "))
for i in range(n):
    while 1:
        n = random()
        if n < 0.5:
            break
    print("dara ke: ",i, '==>', n)
```

## Latihan2
Membuat program untuk menampilkan bilangan terbesar dari n buat data yang diinput, kemudian masukaan angka 0 untuk berhenti.

### Program dan Output

![Gambar2](ssP3/ssP3Lat2.png)

- Langkah-langkah
1. Mencetak "menampilkan bilangan, berhenti ketika bilangan 0, menampilkan bilangan terbesar"
2. bilangan bulat maks = 0
3. Menggunakan fungsi perulangan while true
4. Memasukan bilangan integer pada "a"
5. Menggunakan fungsi if jika max kurang dari nilai a dan max = a
6. Mengunakan fungsi break artinya perulangan berhenti jika menulis nilai 0.
7. Mencetak nilai paling besar.

```bash
max = 0
while True:
    a = int(input("Masukan bilangan = "))
    if max < a:
        max = a
    if a==0:
        break
print("Bilangan Terbesar adalah",max)
```

## Tugas Praktikum3
Membuat program sederhana dengan perulangan: 

Seorang pengusaha menginvestasikan uangnya untuk memulai usahanya dengan modal awal 100 juta,
- Pada bulan pertama dan kedua belum mendapatkan laba
- Pada bulan ketiga mulai mendapatkan laba sebesar 1%
- Pada bulan kelima pendapatan meningkat laba sebesar 5%
- Pada bulan kedepalan mengalami penurunan keuntungan sebesar 2%, sehingga laba menjadi 3%
Hitunglah total keuntungan selama 8 bulan berjalan usahanya!


### Program dan Output

![Gambar3](ssP3/ssP3Lat3.png)

- Langkah-lankah

1. Mencetak "Program menghitung laba dengan modal awal 100 juta"
2. integer a = 100.000.000( modal awal)
3. Menggunakan fungsi looping for pada nilai x 1-9 untuk menampilkan bulan 1 sampai bulan 8.
4. Menggunakan fungsi if, untuk menghitung laba bulan 1 sampai 8
5. Bulan pertama dan kedua laba adalah 0
6. Bulan ke 3 dan ke 4 mendapat laba 1% sehingga modal di kali 1% = keuntungan
7. Bulan ke 5 mendapatkan laba 5%, sehingga modal dikali 5% = keuntungan
8. Bulan ke 8 mmendapatkan penurunan laba 2% sehingga keuntungan menurun dari bulan sebelumnya, modal dikali 3% = keuntungan.
9. Menghitung jumlah total laba dengan menjumlah keuntungan dari bulan ke 1 sampai bulan 8, hasilnya adalah total keuntungan yang didapat.


```bash
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
```

## Terima kasih