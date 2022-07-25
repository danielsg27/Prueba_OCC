import cv2
import numpy as np 
import matplotlib.pyplot as plt

# ROI = x,y w,h
# 200,260,700,80
# 200,240, 400, 60
# 260,280, 440, 80
x = 260 
y = 280 
w = 440
h = 60

kernel = np.ones((5, 5), np.uint8)

im=np.array(cv2.imread("/media/danielsg27/0C78-D0E6/Pruebas_OCC/Capturas/IMG_0001.jpg"))
im2= im[y:y+h, x:x+w]
redim = cv2.resize(im2, (700,len(im2)))
"""imgGray = cv2.cvtColor(im2, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray, (5,5), 1)
ret, th = cv2.threshold(imgBlur,100,255,cv2.THRESH_BINARY) #30-50  #obtu 200 con 75
"""
imgGray = cv2.cvtColor(redim, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray, (5,5), 3)
ret, th = cv2.threshold(imgBlur,100,255,cv2.THRESH_BINARY) #30-50  #obtu 200 con 75




########
img2=th.copy()
h,w=img2.shape
mask=np.zeros((h+2,w+2),np.uint8)
cv2.floodFill(img2,mask,(0,0),255)

#cv2.imshow('relleno',img2)




"""for fila in range (9):
    for columna in range (9):
        print("Color", "fila:", +fila, "columna", +columna, "=", str(th[fila,columna]))
"""


"""imgBin=np.asarray(th)
for i in range(len(imgBin)):
    for j in range(len(imgBin[0])):
        print(imgBin[i][j])"""



#cv2.imshow('Binarizada',th)
        
        
#cv2.imshow('img',im2)
#cv2.imshow('th',th)
"""
plt.imshow(th[:,:],vmin=0,vmax=1)
plt.title("canal Blanco")
plt.figure()
"""
"""hist = cv2.equalizeHist(th)
#hist = cv2.calcHist([imgGray], [0], None, [256], [0, 256])
#hist = cv2.equalizeHist([th], [0], None, [256], [0, 256])
plt.plot(hist, color='gray')

plt.xlabel('intensidad de iluminación')
plt.ylabel('cantidad de pixeles')
plt.show()"""


hist = cv2.equalizeHist(th)

cv2.imshow('Binarizada', hist)



#imgHSV = cv2.cvtColor(im, cv2.COLOR_BGR2HSV)
imgGray = cv2.cvtColor(im2, cv2.COLOR_BGR2GRAY)
imgBin = cv2.threshold(imgGray, 127, 255, cv2.THRESH_BINARY)


#red_lower = np.array([136,87,111],np.uint8)
#red_upper = np.array([180,255,255],np.uint8)
#red_mask = cv2.inRange(imgHSV, red_lower, red_upper)


imgBlur = cv2.GaussianBlur(imgGray, (5,5), 1)
imgCanny = cv2.Canny(th, 100, 320)
imgDialation = cv2.dilate(imgCanny, kernel, iterations=1)
imgEroded = cv2.erode(imgDialation, kernel, iterations=1)
#im2= im[490:550, 200:900]
#im2= im[x:x+w, y:y+h]
#cv2.imshow('Binary',imgBin)
#cv2.imshow('imagen2',im2)

cv2.imwrite("/media/danielsg27/0C78-D0E6/Pruebas_OCC/Capturas/Capturas_ROI/ROI_1.jpg",im2)
#cv2.imwrite("/media/danielsg27/0C78-D0E6/Pruebas_OCC/Capturas/Capturas_ROI/ROI_1_HSV.jpg",imgHSV)
cv2.imwrite("/media/danielsg27/0C78-D0E6/Pruebas_OCC/Capturas/Capturas_ROI/ROI_1_GRAY.jpg",imgGray)
cv2.imwrite("/media/danielsg27/0C78-D0E6/Pruebas_OCC/Capturas/Capturas_ROI/ROI_1_BIN.jpg",th)
cv2.imwrite("/media/danielsg27/0C78-D0E6/Pruebas_OCC/Capturas/Capturas_ROI/ROI_1_Dia.jpg",imgDialation)
cv2.imwrite("/media/danielsg27/0C78-D0E6/Pruebas_OCC/Capturas/Capturas_ROI/ROI_1_Canny.jpg",imgCanny)
cv2.waitKey(0)
cv2.destroyAllWindows()
