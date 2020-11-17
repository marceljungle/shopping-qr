from pyzbar.pyzbar import decode
from PIL import Image

dec = decode(Image.open('QRCode.png'))
print(str(dec[0].data)[1:])
