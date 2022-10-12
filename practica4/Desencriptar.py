import base64


def decode_file1():
    with open('mystery_img1.txt', 'rb') as image_dec:
        imagen_bytes = image_dec.readlines()
        imagen_str = b''
        for i in imagen_bytes:
            imagen_str += i
    with open('imagen1.png', 'wb') as imagen_final:
        imagen_data = base64.decodebytes(imagen_str)
        imagen_final.write(imagen_data)

def decode_file2():
    with open('mystery_img2.txt', 'rb') as image_dec:
        imagen_bytes = image_dec.readlines()
        imagen_str = b''
        for i in imagen_bytes:
            imagen_str += i
    with open('imagen2.png', 'wb') as imagen_final:
        imagen_data = base64.decodebytes(imagen_str)
        imagen_final.write(imagen_data)


decode_file1()
decode_file2()