import pyqrcode
import png
from pyqrcode import QRCode

import uuid

s = str(uuid.uuid4())

url = pyqrcode.create(s)

url.png("myqr5.png", scale=8)
