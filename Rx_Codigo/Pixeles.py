import cv2
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as img
import re
#from statistics import mode
import os

datos=[]
#binarios=[]
#letra=[]
x = 0 
y = 0 
w = 600
h = 0
corte_blanco=0
corte_negro=0

main_path = '/home/danielsg27/Documentos/Caps/Pruebas_LuzAmbiente/'
path = main_path + 'Binarizadas_LuzAmbiente/'
filenames = os.listdir(path)
header = 'cap_2022_01_01_'

n=20 #numero de pixeles aprox por franja con 800us


for file in filenames:
    print(file)
    im=np.array(cv2.imread(path+file))
    h=len(im)
    for i in range(1,len(im[0]),1):
        (b, g, r) = im[40][i]
        if (b >= 250 and g >= 250 and r >= 250):
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
    im2= im[y:y+h, x:x+w]
    cv2.imwrite(main_path+"Imagen_Binarios/Binarios_"+file,im2)
    for j in range(0,len(im2[0]),1):
        (b, g, r) = im2[40][j]
        if (b >= 250 and g>=250 and r>=250):
            datos.append("1")
        elif(b <= 10 and g<=10 and r<=10):
            datos.append("0")
    strBin_com = "".join(datos)
    new_strBin_com = strBin_com.replace('10',',')
    new_strBin_com1 = new_strBin_com.replace('01',',')
    bin_separado = new_strBin_com1.split(",")
    binarios_final=[]
    for num_bin in bin_separado:
        if(len(num_bin)>0.5*n and len(num_bin)<= 1.5*n):
            binarios_final.append(num_bin[0])
        elif(len(num_bin)>1.5*n and len(num_bin)<=2.5*n):
            binarios_final.append(num_bin[0])
            binarios_final.append(num_bin[0])
        elif(len(num_bin)>2.5*n):
            binarios_final.append(num_bin[0])
            binarios_final.append(num_bin[0])
            binarios_final.append(num_bin[0])
            binarios_final.append(num_bin[0])
    #print(binarios_final)
    strBin = "".join(binarios_final)
    print(strBin)
    corte_blanco=0
    corte_negro=0
    x=0
    h=0
    datos=[]

#########Para sacar los datos de una letra en 16 bits #####
#########no funciona bien####
"""try:
    found=re.search('111(.+?)111',strBin).group(1)
    print(found)
except AtributteError:
    pass"""
  
cv2.waitKey(0)
cv2.destroyAllWindows()
