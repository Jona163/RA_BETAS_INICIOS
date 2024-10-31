import cv2
import numpy as np
import cv2.aruco as aruco

aruco = cv2.aruco
# Inicializa la cámara
cap = cv2.VideoCapture(0)

# Cargar el diccionario de ArUco
aruco_dict = aruco.getPredefinedDictionary(aruco.DICT_6X6_250)
parameters = aruco.DetectorParameters()  # Cambia esto a DetectorParameters()

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Detectar marcadores en el frame
    corners, ids, rejected = aruco.detectMarkers(frame, aruco_dict, parameters=parameters)
    if ids is not None:
        # Dibuja los contornos de los marcadores
        aruco.drawDetectedMarkers(frame, corners, ids)
       
        # Ejemplo: sobreponiendo un cuadro
        for corner in corners:
            # Coordenadas de la esquina superior izquierda del marcador
            top_left = tuple(corner[0][0].astype(int))
            bottom_right = tuple(corner[0][2].astype(int))
            cv2.rectangle(frame, top_left, bottom_right, (0, 255, 0), 2)

    # Muestra el frame con la realidad aumentada
    cv2.imshow("Realidad Aumentada", frame)
