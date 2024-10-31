import cv2
import cv2.aruco as aruco

# Verifica si detectMarkers está disponible
try:
    aruco.detectMarkers  # Solo para verificar la existencia
    print("detectMarkers está disponible.")
except AttributeError:
    print("detectMarkers NO está disponible.")

