import cv2
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as img
import re
from statistics import mode


datos=[]
binarios=[]
#letra=[]
x = 0 
y = 0 
w = 0
h = 0

im=np.array(cv2.imread("/home/danielsg27/Documentos/Capturas/Capturas_ROI/ROI_1_BIN.jpg"))

print(len(im))
h=len(im)
print(len(im[0]))

n=20  ###Numero de pixeles que ocupan una franja en la imagen
####Sector de ROI#####
######################
for j in range(1,len(im[0]),1):
    (b, g, r) = im[40][j]
    if (b >= 250 ):
        x += j 
        print(x)
        break
        
for j in range(len(im[0])-1,0,-1):
    (b, g, r) = im[40][j]
    if (b >= 250 ):
        w = j-x
        print(w)
        break
  
  
im2= im[y:y+h, x:x+w]
cv2.imshow('Binarizada', im2)


###############Es para ajustar bien la lectura de los pixeles###########################
print(x)
print(w)

pixel= (w-x)%n
inicio=0
if(pixel<=4):
    inicio=pixel-3
elif(pixel<=6):
    inicio=pixel    
elif(pixel<=8):
    inicio=pixel-1
elif(pixel<=10):
    inicio=pixel-2    
elif(pixel<=12):
    inicio=pixel-3
elif(pixel<=14):
    inicio=pixel-4
elif(pixel<=16):
    inicio=pixel-5
elif(pixel<=18):
    inicio=pixel
    
print(pixel)
print(inicio)

#####Recorrer la zona central para sacarlos valores
for j in range(inicio,len(im2[0]),1):
    (b, g, r) = im2[40][j]
    #(b1, g1, r1) = im[30][j]
    #(b2, g2, r2) = im[31][j]
    #print(im[24][j])
    #print(im[29][j])
    #print(b)
    if (b >= 250):
        datos.append(1)
    elif(b <= 10):
        datos.append(0)

listas=[datos[i:i+n] for i in range(0, len(datos), n)]
#print(listas)

for lista in listas:
    binarios.append(str(mode(lista)))
    #print(mode(lista))



print(binarios)
strBin = "".join(binarios)
print(strBin)


#########Para sacar los datos de una letra en 16 bits #####
#########no funciona bien####
try:
    found=re.search('111(.+?)11110',strBin).group(1)
    print(found)
except AtributteError:
    pass

#print(datos)  
cv2.waitKey(0)
cv2.destroyAllWindows()
