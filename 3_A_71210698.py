def hitung_hapus():
    kalimat = input("Masukkan kalimat: ")
    start = int(input("Index Start: "))
    stop = int(input("Index Stop: "))
    hasil = ((stop-start+1)/len(kalimat))*100
    if hasil < 0:
        return 0.0
    else:
        return hasil
print(hitung_hapus())
    