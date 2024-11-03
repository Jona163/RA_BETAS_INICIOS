import cv2
import numpy as np
import qrcode
from matplotlib import pyplot as plt
import cv2.aruco as aruco
# Función para generar un código QR
def generate_qr(image_filename, qr_filename):
