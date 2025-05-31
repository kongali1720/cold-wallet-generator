# utils/qr_generator.py

import qrcode

def create_qr(data, filename):
    qr = qrcode.make(data)
    qr.save(filename)
