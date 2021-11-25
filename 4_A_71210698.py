def ambildanbalik(kalimat,indexmulai,indexakhir,Tof):
    if Tof == True:
        hasil = kalimat[indexakhir-1:indexmulai-2:-1]
    else:
        hasil = kalimat[indexmulai-1:indexakhir ]
    return hasil
print(ambildanbalik("abcdefg",2,4,True))
print(ambildanbalik("abcdefg",1,5,False))
print(ambildanbalik("Qwerty",3,4,True))
print(ambildanbalik("Qwerty",2,2,False))