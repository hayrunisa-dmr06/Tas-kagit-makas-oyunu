import random

def tas_kagit_makas_Hayrunisa_Demir():
    # Seçenekler ve puanlar
    secenekler = ['tas', 'kagit', 'makas']
    oyuncu_puani = 0
    bilgisayar_puani = 0
    
    while oyuncu_puani < 2 and bilgisayar_puani < 2:
        print("\nMerhabalar Tas, Kagit, Makas oyununa hoş geldiniz!")
        print(f"Şu anki skor - Oyuncu: {oyuncu_puani}, Bilgisayar: {bilgisayar_puani}")
        
        # Kullanıcının seçimi
        oyuncu_secimi = input("Lütfen tas, kagit, makastan birini secin. (tas, kagit, makas): ").lower()
        while oyuncu_secimi not in secenekler:
            oyuncu_secimi = input("Geçersiz seçim, lütfen tekrar deneyin (tas, kagit, makas): ").lower()
        
        # Bilgisayarın seçimi
        bilgisayar_secimi = random.choice(secenekler)
        print(f"Bilgisayarın seçimi: {bilgisayar_secimi}")
        
        # Oyun kuralları
        if oyuncu_secimi == bilgisayar_secimi:
            print("Berabere!")
        elif (oyuncu_secimi == 'tas' and bilgisayar_secimi == 'makas') or \
             (oyuncu_secimi == 'kagit' and bilgisayar_secimi == 'tas') or \
             (oyuncu_secimi == 'makas' and bilgisayar_secimi == 'kagit'):
            print("Bu turu siz kazandınız!")
            oyuncu_puani += 1
        else:
            print("Bu turu bilgisayar kazandı!")
            bilgisayar_puani += 1

        # Oyuna devam mı?
        tekrar_oyna = input("Başka bir oyun oynamak istiyor musunuz? (evet/hayır): ").lower()
        bilgisayar_tekrar = random.choice(['evet', 'hayır'])
        print(f"Bilgisayarın isteği: {bilgisayar_tekrar}")
        
        if tekrar_oyna != 'evet' or bilgisayar_tekrar != 'evet':
            print("Oyun sona erdi!")
            break
    
    # Kazananı belirleme
    if oyuncu_puani == 2:
        print("Tebrikler! Oyunu kazandınız!")
    elif bilgisayar_puani == 2:
        print("Tebrikler bilgisayar oyunu kazandı!")
    else:
        print("Oyun tamamlanmadı.")

# Fonksiyonu çalıştırmak için:
tas_kagit_makas_Hayrunisa_Demir()