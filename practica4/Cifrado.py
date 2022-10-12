import base64


def encode_file():
    with open('hola_mundo.c', 'rb') as hola_mundo:
        texto_data = hola_mundo.read()
        texto_base64 = base64.b64encode(texto_data)
        texto_inf = texto_base64.decode('utf-8')

    with open('Hola_Mundo.txt', 'w+') as texto_final:
        texto_final.write(texto_inf)


encode_file()
