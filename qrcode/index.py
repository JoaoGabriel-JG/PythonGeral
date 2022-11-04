# coding and enconding qrcode
import qrcode

data = 'https://github.com/JoaoGabriel-JG'

qr = qrcode.QRCode(version = 1, box_size = 10, border = 5)

qr.add_data(data)

qr.make(fit = True)
img = qr.make_image(fill_color = 'blue', back_color = 'white')

img.save('/home/joao.gabriel/Documentos/a/qrcodeGitHub2.png')

"""
img = qrcode.make(data)
img.save('/home/joao.gabriel/Documentos/a/qrcodeGitHub.png')
"""