import qrcode 

info = input("Name & Number:")

img = qrcode.make(info)
img.save("info.png")