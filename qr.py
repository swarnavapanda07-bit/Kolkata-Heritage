import qrcode

url = "https://kolkata-heritage.onrender.com"

qr = qrcode.make(url)

qr.save("kolkata_qr.png")

print("QR Code generated successfully!")
print("QR Code URL:", url)