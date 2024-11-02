import cv2
import numpy as np
import cv2.aruco as aruco
import qrcode
from matplotlib import pyplot as plt

# Función para generar un código QR
def generate_qr(image_filename, qr_filename):
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(image_filename)
    qr.make(fit=True)
    qr_image = qr.make_image(fill_color="black", back_color="white")
    qr_image.save(qr_filename)
    print(f"Código QR guardado como: {qr_filename}")
