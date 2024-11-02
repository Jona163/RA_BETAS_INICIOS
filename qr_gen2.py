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

# Función para cargar y mostrar una imagen
def load_image(image_filename):
    image = cv2.imread(image_filename)
    if image is None:
        print("Error al cargar la imagen.")
        return None
    return cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Función para mostrar la imagen en 3D
def display_image_in_3d(image):
    plt.imshow(image)
    plt.axis('off')  # Ocultar ejes
    plt.show()

# Cargar la imagen que quieres usar
image_filename = input("Ingresa el nombre del archivo de imagen: ")
qr_filename = "qr_code.png"
generate_qr(image_filename, qr_filename)
