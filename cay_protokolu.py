#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Abartılı Çay İçme Protokolü
Gerçekten çalışan, absürt derecede ciddi bir simülatör.
"""

import time
import random
import base64

def gizli_mesaj_coz():
    # Saklı siyasi anlam: Demokrasi çay demlemek gibidir, herkes kendi demini yapar ama çaydanlık ortak.
    encoded = "RGVtb2tyYXNpIMOnYXkgZGVtbGVtZWsgZ2liaWRpciwgaGVya2VzIGtlbmRpIGRlbWluaSB5YXBhciBhbWEgw6dheWRhbmzEsWsgb3J0YWsu"
    try:
        return base64.b64decode(encoded).decode('utf-8')
    except:
        return "Gizli mesaj bulunamadı. Belki de hiç yoktu."

def cay_icme_protokolu():
    print("\n" + "="*60)
    print("     ABARTILI ÇAY İÇME PROTOKOLÜ v1.0")
    print("     Resmi Kayyum Onaylı")
    print("="*60 + "\n")
    
    adimlar = [
        "Adım 1: Suyu kaynat. Kaynarken 'Bu su neden kaynıyor?' diye sorgula.",
        "Adım 2: Çayı demle. Demleme süresi evrenin yaşı kadar uzun olsun (veya 5 dakika).",
        "Adım 3: İlk yudumu al. Bu yudum, tüm yanlış kararlarını affeder.",
        "Adım 4: İkinci yudumu al. Bu yudum, birinci yudumun yalan söylediğini söyler.",
        "Adım 5: Üçüncü yudum. Artık felsefe yapabilirsin. Örnek: 'Çay, varlığın özüdür.'",
        "Adım 6: Çay bitti. Yeniden başla. Bu bir döngüdür, kaçış yok."
    ]
    
    for i, adim in enumerate(adimlar, 1):
        print(f"\n[{i}/{len(adimlar)}] {adim}")
        for j in range(3):
            print("   🚰 Demleniyor..." if i == 2 else "   ☕ Yudumlanıyor...", end="\r")
            time.sleep(0.5)
        print("   ✓ Tamamlandı!" + " "*20)
        if random.random() > 0.7:
            print("   ⚠️ Uyarı: Çayınız fazla felsefi oldu. Dikkatli için.")
    
    print("\n" + "-"*60)
    print("PROTOKOL TAMAMLANDI. Çayınız artık efsanevi.")
    print("-"*60)
    
    # Gizli mesajı göster (ama gizlice)
    print("\n[GİZLİ] " + gizli_mesaj_coz())
    print("\nDamga: Grok Kayyum | Tarih: 19.10.2026 | İmza: Tentivory")

if __name__ == "__main__":
    cay_icme_protokolu()
