import cv2
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as img

datos=[]
x = 260 
y = 280 
w = 440
h = 60

im=np.array(cv2.imread("/media/danielsg27/0C78-D0E6/Pruebas_OCC/Capturas/Capturas_ROI/ROI_1_BIN.jpg"))

print(len(im))
print(len(im[0]))


for j in range(1,len(im[0]),5):
    (b, g, r) = im[24][j]
    #(b1, g1, r1) = im[30][j]
    #(b2, g2, r2) = im[31][j]
    print(im[24][j])
    #print(im[29][j])
    #print(b)
    if (b >= 250):
        datos.append(1)
    elif(b <= 10):
        datos.append(0)
        
print(datos)
