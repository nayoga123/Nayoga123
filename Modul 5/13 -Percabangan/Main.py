# percabangan 
# struktur
"""
    1.if -nya
    2.punya kondisi
    3.punya aksi
"""
nama = input ("masukkan nama : ")

# percabanga yang inline (satu baris)
#if nama == "yoga": print("selamat datang")
#print("terima kasih")

#percabangan indentasi
#if nama == "yoga" :
#print("selamat datang")
#print("selamat belajar pyton")
#print("bukan bagian percabangan")

# percabangan 1 kondisi dan 2 aksi
# pakai kata kunci 'else'

if nama == "yoga" :
        print(f"selamat datang {nama}")
else :
        print(f'Anda {nama}, bukan adam')
print("Terima kasih")