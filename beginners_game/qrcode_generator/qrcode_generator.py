import qrcode
import qrtools


# =============== encode data ==============

def generate_qr_code(username):
    img = qrcode.make(username)
    img.save(f"{username}.png")
    print("QR CODE CREATED SUCCESSFULLY")


userName = input("Type your name: ")
generate_qr_code(userName)


# =========== decode data ===============


def decode_qr_image(imagePath):
    qr = qrtools.QR()
    qr.decode(imagePath)
    print(f"the content of the QR image id : {qr.data}")


decode_qr_image(f"{userName}.png")
