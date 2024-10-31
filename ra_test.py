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
