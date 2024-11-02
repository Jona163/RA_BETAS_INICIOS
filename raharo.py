#pip install PyOpenGL PyOpenGL_accelerate
import cv2
import numpy as np
import cv2.aruco as aruco
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

# Inicializa la cámara
cap = cv2.VideoCapture(0)

# Cargar el diccionario de ArUco
aruco_dict = aruco.getPredefinedDictionary(aruco.DICT_6X6_250)
parameters = aruco.DetectorParameters()

# Cargar la imagen que quieres mostrar
image_to_render = cv2.imread('ruta/a/tu/imagen.png')  # Cambia esto a la ruta de tu imagen
image_to_render = cv2.flip(image_to_render, 0)  # Voltear la imagen para OpenGL

# Configuración de OpenGL
def render_2d_image(x, y, image):
    glEnable(GL_TEXTURE_2D)
    glBindTexture(GL_TEXTURE_2D, texture_id)

    glBegin(GL_QUADS)
    glTexCoord2f(0, 1)
    glVertex3f(x - 1, y - 1, 0)  # Esquina inferior izquierda
    glTexCoord2f(1, 1)
    glVertex3f(x + 1, y - 1, 0)  # Esquina inferior derecha
    glTexCoord2f(1, 0)
    glVertex3f(x + 1, y + 1, 0)  # Esquina superior derecha
    glTexCoord2f(0, 0)
    glVertex3f(x - 1, y + 1, 0)  # Esquina superior izquierda
    glEnd()

    glDisable(GL_TEXTURE_2D)

# Crear textura OpenGL
texture_id = glGenTextures(1)
glBindTexture(GL_TEXTURE_2D, texture_id)
glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, image_to_render.shape[1], image_to_render.shape[0], 0, GL_BGR, GL_UNSIGNED_BYTE, image_to_render)
glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Detectar marcadores en el frame
    corners, ids, rejected = aruco.detectMarkers(frame, aruco_dict, parameters=parameters)
    if ids is not None:
        # Dibuja los contornos de los marcadores
        aruco.drawDetectedMarkers(frame, corners, ids)

        # Renderizar imagen 3D en la ubicación del marcador
        for i, corner in enumerate(corners):
            # Obtener coordenadas del marcador
            top_left = tuple(corner[0][0].astype(int))
            bottom_right = tuple(corner[0][2].astype(int))
            center_x = (top_left[0] + bottom_right[0]) / 2
            center_y = (top_left[1] + bottom_right[1]) / 2

            # Renderizar la imagen 2D
            render_2d_image(center_x, center_y, image_to_render)
