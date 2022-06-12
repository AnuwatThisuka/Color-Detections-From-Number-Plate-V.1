import cv2
from cv2 import resize
import numpy as np
import pytesseract
import os
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r"C://Program Files//Tesseract-OCR//tesseract.exe"

img = cv2.imread(
    "C:\\Users\\Acer\\Desktop\\IIOT-B14-Project\\Auto_Paining\\Model\\Model-1.jpg")
img = resize(img, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_CUBIC)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
adaptive_threshold = cv2.adaptiveThreshold(
    gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 85, 11)
text = pytesseract.image_to_string(
    adaptive_threshold, lang='eng', config='--psm 8')
print(text)
