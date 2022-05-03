import qrcode
#from qrtools import qrtools
from PIL import Image
from pyzbar.pyzbar import decode


# =============== encode data ==============

def generate_qr_code(filename, data):
    img = qrcode.make(data)
    img.save(f"{filename}.png")
    print("QR CODE CREATED SUCCESSFULLY")


userName = input("Type your name: ")
final = userName.replace(" ","_")
generate_qr_code(final, userName)


# =========== decode data ===============


def decode_qr_image(imagePath):
    #qr = qrtools.QR()
    data = decode(Image.open(imagePath))
    print(f"the content of the QR image id : {data.data}")


final = userName.replace(" ","_")
decode_qr_image(f"{final}.png")
