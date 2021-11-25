def ambil_tengah(a,b = 0):
    panjang_kalimat = len(a)
    if panjang_kalimat%2 == 0:
       index_tengah = (panjang_kalimat / 2)
    else:
        index_tengah = panjang_kalimat//2
    hasil = a[int(index_tengah)+b]

    return hasil 
print(ambil_tengah("abcdefg",1))
print(ambil_tengah("abcdefg",2))
print(ambil_tengah("abcd"))