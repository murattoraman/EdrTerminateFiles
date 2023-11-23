import keyboard

def on_press(key):
    # Tuşun değerini yazdır
    print(key)

# Klavye dinleyiciyi başlat
keyboard.on_press(on_press)

# Bekle
while True:
    # Kullanıcının `q` tuşuna basması durumunda kodu sonlandır
    if keyboard.is_pressed("q"):
        print("Çıkış")
        exit()