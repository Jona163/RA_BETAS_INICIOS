import cv2
import numpy as np
import cv2.aruco as aruco

aruco = cv2.aruco
# Inicializa la cámara
cap = cv2.VideoCapture(0)

# Cargar el diccionario de ArUco
aruco_dict = aruco.getPredefinedDictionary(aruco.DICT_6X6_250)
parameters = aruco.DetectorParameters()  # Cambia esto a DetectorParameters()
