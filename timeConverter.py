def timeConverter(seconds):                       #Buat nama fungsi dan masukan parameter
    import math                                   #memanggil library matematika
    seconds=int(input('Masukan detik:'))          #tulis variabel untuk menginput data
    if seconds<=359999 and seconds>=0:            #buat kondisi detik yang dimasukan tidak boleh lebih dari 359999 dan minus
        jam=math.floor(seconds/3600)              #menentukan jam dengan membagi detik yang dimasukan dan menggunakan math.floor agar hasil desimal dibulatkan kebawah
        menit=math.floor((seconds-(jam*3600))/60) #menentukan menit dengan mengurangi detik yang di masukan dengan jam
        detik=math.floor(seconds-(jam*3600)-(menit*60))      #menentukan detik dengan mengurangi detik yang di masukan dengan variabel jam dan menit
        print('Konversi :',str(jam),':', str(menit),':',str(detik))   #print variabel dalam kondisi diatas dengan menambahkan str agar type data berubah
    else:
        print('Invalid Input!')                   #Jika detik yang dimasukan tidak sesuai kondisi maka akan print Invalid Input!
timeConverter(3665)                            #memanggil fungsi timeConverter
