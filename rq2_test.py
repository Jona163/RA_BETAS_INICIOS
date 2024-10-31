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
if image_to_render is not None:
    image_to_render = cv2.cvtColor(image_to_render, cv2.COLOR_BGR2RGB)

# Inicializa la cámara
cap = cv2.VideoCapture(0)

# Inicializa el diccionario y los parámetros de ArUco
aruco_dict = aruco.Dictionary_get(aruco.DICT_6X6_250)
parameters = aruco.DetectorParameters_create()
qr_detector = cv2.QRCodeDetector()

# Bucle principal para procesar el video en tiempo real
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        print("No se pudo capturar el frame de la cámara.")
        break

    # Detectar marcadores ArUco en el frame
    corners, ids, _ = aruco.detectMarkers(frame, aruco_dict, parameters=parameters)

    # Dibuja los marcadores ArUco en la imagen
    if ids is not None:
        aruco.drawDetectedMarkers(frame, corners, ids)

    # Detectar el código QR en el frame
    qr_data, points, _ = qr_detector.detectAndDecode(frame)
    if qr_data:
        print("Código QR detectado:", qr_data)

        # Mostrar la imagen 3D sobre el marcador en la cámara
        if image_to_render is not None:
            # Redimensionar la imagen a renderizar para ajustarse a un área de la ventana
            h, w, _ = image_to_render.shape
            resized_image = cv2.resize(image_to_render, (w // 2, h // 2))

            # Determinar la posición de la imagen renderizada en el frame
            y_offset, x_offset = 50, 50
            frame[y_offset:y_offset + resized_image.shape[0], x_offset:x_offset + resized_image.shape[1]] = resized_image

    # Mostrar el frame en una ventana
    cv2.imshow("Realidad Aumentada con QR", frame)

    # Presionar 'q' para salir del bucle
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberar la cámara y cerrar ventanas
cap.release()
cv2.destroyAllWindows()
