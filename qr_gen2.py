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

# Cargar el código QR y mostrarlo
qr_image = cv2.imread(qr_filename)
if qr_image is not None:
    plt.imshow(qr_image)
    plt.axis('off')  # Ocultar ejes
    plt.show()

# Inicializa la cámara
cap = cv2.VideoCapture(0)
# Cargar el diccionario de ArUco
aruco_dict = aruco.getPredefinedDictionary(aruco.DICT_6X6_250)
parameters = aruco.DetectorParameters()

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Detectar marcadores en el frame
    corners, ids, rejected = aruco.detectMarkers(frame, aruco_dict, parameters=parameters)
    if ids is not None:
        # Dibuja los contornos de los marcadores
        aruco.drawDetectedMarkers(frame, corners, ids)
       
        # Procesar cada marcador detectado
        for corner in corners:
            # Leer QR
            qr_data, _ = cv2.QRCodeDetector()(frame)
            if qr_data:
                print("Código QR detectado: ", qr_data)
                # Cargar la imagen desde la ruta del QR
                image_to_render = load_image(qr_data)
                if image_to_render is not None:
                    display_image_in_3d(image_to_render)  # Mostrar la imagen en 3D

    # Muestra el frame
    cv2.imshow("Realidad Aumentada", frame)
