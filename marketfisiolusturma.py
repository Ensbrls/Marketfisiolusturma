def tekrar():
    print()
    urunsayi = int(input("Kaç Ürününüz Var?: "))

    isimler = []
    fiyatlar = []
    count = 0

    for i in range(1,urunsayi+1):
        count = count + 1

        urunisim = input(f"{count}.Ürünün İsmi Nedir?: ").strip().title()
        urunfiyat = float(input(f"{count}.Ürünün Fiyatı Nedir?: "))

        isimler.append(urunisim)
        fiyatlar.append(urunfiyat)


    print(f"\nÜrün\t\tFiyat\n{'-'*25}")

    for i in range(urunsayi):
        print(f"{isimler[i]}\t\t{fiyatlar[i]:.2f} TL")

    print(f"{'-'*25}\nToplam:\t\t{sum(fiyatlar):.2f} TL \n")

    tekrarsoru = input("Tekrar Market Fişi Oluşturmak İstermisiniz? (E/H): ").lower()
    if tekrarsoru == "e":
        tekrar()
    else:
        print("Birdaha Görüşmek Üzere!")
tekrar()