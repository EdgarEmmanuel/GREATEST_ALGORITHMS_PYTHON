import qrcode
from qrtools import qrtools
from PIL import Image
from pyzbar.pyzbar import decode


# =============== encode data ==============

def generate_qr_code(username):
    img = qrcode.make(username)
    img.save(f"{username}.png")
    print("QR CODE CREATED SUCCESSFULLY")


userName = input("Type your name: ")
final = userName.replace("","_")
generate_qr_code(final)


# =========== decode data ===============


def decode_qr_image(imagePath):
    #qr = qrtools.QR()
    data = decode(Image.open(imagePath))
    print(f"the content of the QR image id : {data}")


final = userName.replace("","_")
decode_qr_image(f"{final}.png")
