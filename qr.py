import qrcode

url = "http://192.168.0.101:5000"

qr = qrcode.make(url)

qr.save("kolkata_qr.png")

print("QR Code generated successfully!")