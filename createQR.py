# Descargar paquetes pyqrcode, pyzbar, Pillow y pypng
import pyqrcode

qr = pyqrcode.create("http://192.168.1.11:5000/shopping?id=1")
qr.png("Producto 1.png", scale=8)
