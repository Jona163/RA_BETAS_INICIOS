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
