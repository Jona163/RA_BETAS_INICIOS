
import cv2
import numpy as np

# Configura el diccionario de ArUco y el ID del marcador
aruco_dict = cv2.aruco.Dictionary_get(cv2.aruco.DICT_6X6_250)
marker_id = 33  # Puedes cambiar este ID (valores entre 0 y el tamaño del diccionario -1)
marker_size = 200  # Tamaño del marcador en píxeles
