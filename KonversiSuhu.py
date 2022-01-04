#program konversi celsius ke satuan lain
print("\n PROGRAM KONVERSI TEMPERATURE\n")
print("1. Celsius\n2. Fahreiheit\n3. Kelvin\n4. Reamur")

while True:
    suhu=(int(input("Masukkan nomor temperatur yang akan dikonversi:\n")))
    if suhu == 1:
     print("Konversi Celsius")
     
     #celsius ke reamur
     celsius = float(input ('Masukkan suhu dalam Celsius\n'))
     print("suhu adalah",celsius, "°Celsius")

     reamur = (4/5) *celsius
     print("Suhu dalam Reamur=", reamur, "°Reamur")

     fahrenheit = (9/5)*(celsius+32)
     print("Suhu dalam fahrenheit=", fahrenheit, "°Fahrenheit")

     kelvin = 273+celsius
     print("Suhu dalam kelvin=", kelvin, "°Kelvin")
    elif suhu == 2:
        print("Konversi Fahrenheit")

        #conversi fahrenheit
        fahrenheit = float(input('Masukkan suhu dalam Fahrenheit =\n'))
        print("suhu adalah",fahrenheit, "°Fahrenheit")

        #fahrenheit ke celsius
        celsius = (5/9)*(fahrenheit-32)
        print("Suhu dalam celsius=", celsius, "°Celsius")

        #fahrenheit ke reamur
        reamur = (4/9)*(fahrenheit-32)
        print("Suhu dalam reamur=", reamur, "°Reamur")

         #fahrenheit ke kelvin
        kelvin = celsius+273
        print("Suhu dalam kelvin=", kelvin, "°Kelvin")
    elif suhu == 3:
        print("Konversi Kelvin")

        #conversi Kelvin
        kelvin = float(input('Masukkan suhu dalam Kelvin =\n'))
        print("suhu adalah",kelvin, "°Kelvin")

        #Kelvin ke celsius
        celsius = kelvin-273
        print("Suhu dalam celsius=", celsius,"°Celsius")

        #kelvin ke reamur
        reamur = (5/4)*celsius
        print("Suhu dalam reamur=", reamur, "°Reamur")

         #kelvin ke fahrenheit
        fahrenheit = (9/5)*(celsius+32)
        print("Suhu dalam fahrenheit=", fahrenheit, "°Fahrenheit")
    elif suhu == 4:
        print("Konversi Reamur")

        #conversi Kelvin
        reamur = float(input('Masukkan suhu dalam Reamur =\n'))
        print("suhu adalah",reamur, "°Reamur")

        #Kelvin ke celsius
        celsius = (5/4)*reamur
        print("Suhu dalam celsius=", celsius,"°Celsius")

        #reamur ke kelvin
        kelvin = celsius+273
        print("Suhu dalam kelvin=", kelvin, "°Kelvin")

         #reamur ke fahrenheit
        fahrenheit = (9/5)*(celsius+32)
        print("Suhu dalam fahrenheit=", fahrenheit, "°Fahrenheit")
        continue
    else:
        print("Hanya tersedia 1 sampai 4")
