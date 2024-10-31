
import cv2
import numpy as np

# Configura el diccionario de ArUco y el ID del marcador
aruco_dict = cv2.aruco.Dictionary_get(cv2.aruco.DICT_6X6_250)
marker_id = 33  # Puedes cambiar este ID (valores entre 0 y el tamaño del diccionario -1)
marker_size = 200  # Tamaño del marcador en píxeles

# Generar el marcador
marker_image = np.zeros((marker_size, marker_size), dtype=np.uint8)
marker_image = cv2.aruco.drawMarker(aruco_dict, marker_id, marker_size, marker_image, 1)

# Guardar la imagen del marcador
cv2.imwrite(f"marker_{marker_id}.png", marker_image)
print(f"Marcador guardado como marker_{marker_id}.png")
