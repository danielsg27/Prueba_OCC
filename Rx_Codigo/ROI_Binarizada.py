import cv2
import numpy as np 
import matplotlib.pyplot as plt
import os

main_path = '/home/danielsg27/Documentos/Caps/Pruebas_LuzAmbiente/'
path = main_path + 'Capturas_LuzAmbiente/'
filenames = os.listdir(path)
header = 'cap_2022_01_01_'


# ROI = x,y w,h
# 200,260,700,80
# 200,240, 400, 60
# 260,280, 440, 80
x = 500 #260
y = 260 
w = 440 #440
h = 80


kernel = np.ones((5, 5), np.uint8)

for file in filenames:
    im = cv2.imread(path+file)
    im2= im[y:y+h, x:x+w]
    redim = cv2.resize(im2, (700,len(im2)))
    imgGray = cv2.cvtColor(redim, cv2.COLOR_BGR2GRAY)
    imgBlur = cv2.GaussianBlur(imgGray, (5,5),cv2.BORDER_ISOLATED)
    ret, th = cv2.threshold(imgBlur,75,255,cv2.THRESH_BINARY) #80
    imBin=np.array(th)
    
    
    cv2.imwrite(main_path+"Binarizadas_LuzAmbiente/ROI_BIN_"+file,th)

cv2.waitKey(0)
cv2.destroyAllWindows()
