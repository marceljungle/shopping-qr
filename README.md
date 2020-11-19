# shopping-qr

## HOW TO USE
- Check your internal IP (Windows - `cmd` -> `ipconfig` or Linux - `bash` -> `ifconfig`).
- Put internal IP in your browser adding the port at the end (default port: `5000`).
- Having the above info, now we need to create QR code.
  - Modify the `pyqrcode.create()` parameter to your address and port plus pasing the id of the product.
    e.g. ("http://YourInternalIP:5000/shopping?id=1"), this will show the product with ID 1 from the Cloudant database.
  - Give it a name and change the scale if necesary modifying the `qr.png()` parameter.
    e.g. ("Producto 1.png", scale=8), this will create a `.png` file called "Producto 1" with a scale of 8.
  - Run `createQR.py`
-  Run `app.py` using Python 3
- Scan the previously generated QR code and get the info of the product in it.
