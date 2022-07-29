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
w = 600
h = 0
corte_blanco=0
corte_negro=0


im=np.array(cv2.imread("/home/danielsg27/Documentos/Capturas/Capturas_ROI/ROI_1_BIN.jpg"))

print(len(im))
h=len(im)
print(len(im[0]))

n=20  ###Numero de pixeles que ocupan una franja en la imagen
####Sector de ROI#####
######################
for i in range(1,len(im[0]),1):
    (b, g, r) = im[40][i]
    if (b >= 250 ):
        corte_blanco += i 
        print(corte_blanco)
        break

for j in range(corte_blanco,len(im[0])-corte_blanco,1):
    (b, g, r) = im[40][j]
    if (b <= 10 ):
        corte_negro += j 
        print(corte_negro)
        break

x=corte_negro


"""for j in range(len(im[0])-1,0,-1):
    (b, g, r) = im[40][j]
    if (b >= 250 ):
        w = j-x
        print(w)
        break"""
  
  
im2= im[y:y+h, x:x+w]
cv2.imshow('Binarizada', im2)


###############Es para ajustar bien la lectura de los pixeles###########################
print(x)
print(w)
    
#####Recorrer la zona central para sacarlos valores
for j in range(0,len(im2[0]),1):
    (b, g, r) = im2[40][j]
    #(b1, g1, r1) = im[30][j]
    #(b2, g2, r2) = im[31][j]
    #print(im[24][j])
    #print(im[29][j])
    #print(b)
    if (b >= 250):
        datos.append("1")
    elif(b <= 10):
        datos.append("0")

#print(datos)
strBin_com = "".join(datos)
new_strBin_com = strBin_com.replace('10',',')
new_strBin_com1 = new_strBin_com.replace('01',',')
#print(strBin_com)
#print(new_strBin_com1)
bin_separado = new_strBin_com1.split(",")
#print(bin_separado)
binarios_final=[]
for num_bin in bin_separado:
    if(len(num_bin)>10 and len(num_bin)<=30):
        binarios_final.append(num_bin[0])
    elif(len(num_bin)>30 and len(num_bin)<=50):
        binarios_final.append(num_bin[0])
        binarios_final.append(num_bin[0])
    elif(len(num_bin)>50):
        binarios_final.append(num_bin[0])
        binarios_final.append(num_bin[0])
        binarios_final.append(num_bin[0])
        binarios_final.append(num_bin[0])
print(binarios_final)


#listas=[datos[i:i+n] for i in range(0, len(datos), n)]
#print(listas)
#print(datos)

#listas2=[]
#dato_in=0
#final=0
#print(datos[len(datos)-1])
"""
for i in range(0,len(datos),1):
    if(datos[i+1]!=datos[i]):
        dato_in=i
        print(dato_in)
    listas2.append(datos[dato_in:i+1])
        #dato_in=i
    #if(datos[len(datos)-1]==datos[len(datos)-2]):
        #break
        
print(listas2)
"""
"""for lista in listas:
    binarios.append(str(mode(lista)))
    #print(mode(lista))
"""


#print(binarios)
strBin = "".join(binarios_final)
#new_strBin = strBin.replace('111','11')
print(strBin)
#print(new_strBin)

#########Para sacar los datos de una letra en 16 bits #####
#########no funciona bien####
try:
    found=re.search('111(.+?)111',strBin).group(1)
    print(found)
except AtributteError:
    pass

#print(datos)   
cv2.waitKey(0)
cv2.destroyAllWindows()
