from pyzbar.pyzbar import decode
from PIL import Image

img = Image.open('/home/joao.gabriel/Documentos/a/qrcodeGitHub.png')

result = decode(img)

print(result)
