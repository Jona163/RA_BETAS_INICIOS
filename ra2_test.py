import cv2
import numpy as np
import qrcode
from matplotlib import pyplot as plt
import cv2.aruco as aruco

# Función para generar un código QR
def generate_qr(image_filename, qr_filename):
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(image_filename)
    qr.make(fit=True)
    qr_image = qr.make_image(fill_color="black", back_color="white")
    qr_image.save(qr_filename)
    print(f"Código QR guardado como: {qr_filename}")

# Generar el código QR para la imagen que deseas mostrar en 3D
image_filename = "bellaa.png"  # Cambia a la imagen que quieres mostrar
qr_filename = "qr_code.png"
generate_qr(image_filename, qr_filename)

# Cargar la imagen 3D que queremos mostrar cuando se detecte el QR
image_to_render = cv2.imread(image_filename)
