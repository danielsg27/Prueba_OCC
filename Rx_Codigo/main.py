import time,sys,threading
import cv2
import sys
import numpy as np

x = 200 
y = 300 
w = 500 
h = 200
n = 24  #dtm=200-n=18 dtm=250-n=24 --  dtm=300-n=30
bits = []

def analyzeImage(id,image):
    global x,y,w,h,bits,n

    #Binary ROI
    im2= image[y:y+h, x:x+w]
    redim = cv2.resize(im2, (3*len(im2[0]),len(im2)))
    imgGray = cv2.cvtColor(redim, cv2.COLOR_BGR2GRAY)
    imgBlur = cv2.GaussianBlur(imgGray, (5,5),5)
    #imgBlur = cv2.blur(imgGray,(10,10))
    #imgBlur = cv2.medianBlur(imgGray,5)
    #imgBlur = cv2.bilateralFilter(imgGray,9,75,75)
    ret, th = cv2.threshold(imgBlur,80,255,cv2.THRESH_BINARY) #80

    #cv2.imshow("image", im2)
    #cv2.imshow("Threshold Binary", th)
    #cv2.imshow("Resize", redim)
    #Get bits
    datos=[]
    w_bits=0  #400    
    corte_blanco=0
    corte_negro=0
    y_image = 0
    
    im=np.array(th)    
    h=len(im)
    
    for i in range(1,len(im[0]),1):        
        avg_color = im[int(h/2)][i]
        if (avg_color >= 250 ):
            corte_blanco += i 
            #print(corte_blanco)
            break

    for j in range(corte_blanco,len(im[0])-corte_blanco,1):
        avg_color = im[int(h/2)][j]
        if (avg_color <= 10 ):
            corte_negro += j 
            #print(corte_negro)
            break
    
    for k in range(len(im[0])-1,0,-1):
        avg_color = im[int(h/2)][k]
        if (avg_color >= 250 ):
            w_bits=k-corte_negro
            print(w_bits)
            print()
            break
    
    
    img2= im[y_image:y_image+h, corte_negro:corte_negro+w_bits]
    cv2.imshow("image_bin_recortada", img2)
    for j in range(0,len(img2[0]),1):
        avg_color = img2[int(h/2)][j]
        if (avg_color >= 250):
            datos.append("1")
        elif(avg_color <= 10):
            datos.append("0")
    #print(datos)
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
            #binarios_final.append(num_bin[0])
            #binarios_final.append(num_bin[0])
            binarios_final.append("-")
            binarios_final.append("-")
            binarios_final.append(num_bin[0])
    
    strBin = "".join(binarios_final)
    print(binarios_final)
    bits.insert(id,strBin)
    print(bits)
    #corte_blanco=0
    #corte_negro=0
    #x=0
    #h=0
    #datos=[]
    


def main():    
    print("Start VLC!")
    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1024)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 600)
    cap.set(cv2.CAP_PROP_FPS, 25)
    cap.set(cv2.CAP_PROP_ISO_SPEED, 800)
    cap.set(cv2.CAP_PROP_BRIGHTNESS,72) #70
    cap.set(cv2.CAP_PROP_CONTRAST,40)
    cap.set(cv2.CAP_PROP_AUTO_EXPOSURE,0.52) #52
    #cap.set(cv2.CAP_PROP_EXPOSURE,0.52) #52
    
    counter=0
    while cap.isOpened():                
        success, image = cap.read()
        if not success:
            sys.exit(
                'ERROR: Unable to read from webcam. Please verify your webcam settings.'
            )

        #image = cv2.flip(image, 1)
        #Configs                
        image=cv2.rotate(image, cv2.ROTATE_90_COUNTERCLOCKWISE)
        if cv2.waitKey(1) == 27:
            break

        thread = threading.Thread(target=analyzeImage,args=[counter,image])
        thread.start()
        cv2.imshow('VLC', image)
        counter += 1
        
    cap.release()
    cv2.destroyAllWindows()


main()

# with picamera.PiCamera() as camera:
#     camera.rotation = -90
#     camera.ISO = 800
#     camera.resolution=(1024,600)
#     camera.shutter_speed = 200 #100 o 180
#     camera.brightness = 85 # 75
#     camera.contrast = 100
#     for i in range (10):
#         time.sleep(0.2) # 200ms
#         camera.capture(path + 'IMG_%04d.jpg' % i)
#     camera.stop_preview()
#     camera.close()
