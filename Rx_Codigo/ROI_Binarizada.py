import cv2
import numpy as np 
import matplotlib.pyplot as plt

# ROI = x,y w,h
# 200,260,700,80
# 200,240, 400, 60
# 260,280, 440, 80
x = 500 #260
y = 260 
w = 440 #440
h = 80

kernel = np.ones((5, 5), np.uint8)

im=np.array(cv2.imread("/home/danielsg27/Documentos/Capturas/IMG_0003.jpg"))
im2= im[y:y+h, x:x+w]
redim = cv2.resize(im2, (700,len(im2)))

"""imgGray = cv2.cvtColor(im2, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray, (5,5), 10)
ret, th = cv2.threshold(imgBlur,100,255,cv2.THRESH_BINARY) #30-50  #obtu 200 con 75
"""
imgGray = cv2.cvtColor(redim, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray, (5,5),cv2.BORDER_ISOLATED)
ret, th = cv2.threshold(imgBlur,80,255,cv2.THRESH_BINARY) #30-50  #obtu 200 con 75





cv2.imshow('Binarizada', th)

#imgHSV = cv2.cvtColor(im, cv2.COLOR_BGR2HSV)
imgGray = cv2.cvtColor(im2, cv2.COLOR_BGR2GRAY)
imgBin = cv2.threshold(imgGray, 127, 255, cv2.THRESH_BINARY)

imgBlur = cv2.GaussianBlur(imgGray, (5,5), 1)
imgCanny = cv2.Canny(th, 100, 320)
imgDialation = cv2.dilate(imgCanny, kernel, iterations=1)
imgEroded = cv2.erode(imgDialation, kernel, iterations=1)
#im2= im[490:550, 200:900]
#im2= im[x:x+w, y:y+h]
#cv2.imshow('Binary',imgBin)
#cv2.imshow('imagen2',im2)

cv2.imwrite("/home/danielsg27/Documentos/Capturas/Capturas_ROI/ROI_1.jpg",im2)
#cv2.imwrite("/media/danielsg27/0C78-D0E6/Pruebas_OCC/Capturas/Capturas_ROI/ROI_1_HSV.jpg",imgHSV)
cv2.imwrite("/home/danielsg27/Documentos/Capturas/Capturas_ROI/ROI_1_GRAY.jpg",imgGray)
cv2.imwrite("/home/danielsg27/Documentos/Capturas/Capturas_ROI/ROI_1_BIN.jpg",th)
cv2.imwrite("/home/danielsg27/Documentos/Capturas/Capturas_ROI/ROI_1_Dia.jpg",imgDialation)
cv2.imwrite("/home/danielsg27/Documentos/Capturas/Capturas_ROI/ROI_1_Canny.jpg",imgCanny)
cv2.waitKey(0)
cv2.destroyAllWindows()
