# Descargar paquetes pyqrcode, pyzbar, Pillow y pypng
import pyqrcode

qr = pyqrcode.create("www.google.com")
qr.png("QRCode.png", scale=8)
