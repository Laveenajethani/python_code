import pyqrcode
from pyqrcode import QRCode
a="www.google.com"
url=pyqrcode.create(a)
url.svg('myqr.svg,scale=3')
