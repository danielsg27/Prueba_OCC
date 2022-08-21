import time,sys,threading
import cv2
import sys
import numpy as np
import math

x = 200 
y = 300 
w = 500 
h = 200
n = 18  #dtm=200-n=18 dtm=250-n=24 --  dtm=300-n=30 por el redim de 3
        #n=7.5 en 250  
bits = []
counter = 0
texto_final = ''


#Variables for text
enter = "1010101010101010"
dict_letters_zero = {"1001101010101001": { "letter" : "A", "count": 0}, "1001011010101001": { "letter" : "a", "count": 0}, "1001011010100110": { "letter" : "b", "count": 0}, "1001101010100110": { "letter" : "B", "count": 0},"1001011010100101": { "letter" : "c", "count": 0}, "1001101010100101": { "letter" : "C", "count": 0} , "1001011010011010": { "letter" : "d", "count": 0}, "1001101010011010": { "letter" : "D", "count": 0}, "1001011010011001": { "letter" : "e", "count": 0}, "1001101010011001": { "letter" : "E", "count": 0}, "1001011010010110": { "letter" : "f", "count": 0}, "1001101010010110": { "letter" : "F", "count": 0}, "1001011010010101": { "letter" : "g", "count": 0}, "1001101010010101": { "letter" : "G", "count": 0}, "1001011001101010": { "letter" : "h", "count": 0}, "1001101001101010": { "letter" : "H", "count": 0}, "1001011001101001": { "letter" : "i", "count": 0}, "1001101001101001": { "letter" : "I", "count": 0}, "1001011001100110": { "letter" : "j", "count": 0}, "1001101001100110": { "letter" : "J", "count": 0}, "1001011001100101": { "letter" : "k", "count": 0}, "1001101001100101": { "letter" : "K", "count": 0}, "1001011001011010": { "letter" : "l", "count": 0}, "1001101001011010": { "letter" : "L", "count": 0}, "1001011001011001": { "letter" : "m", "count": 0}, "1001101001011001": { "letter" : "M", "count": 0}, "1001011001010110": { "letter" : "n", "count": 0}, "1001101001010110": { "letter" : "N", "count": 0}, "1001011001010101": { "letter" : "o", "count": 0}, "1001101001010101": { "letter" : "O", "count": 0}, "1001010110101010": { "letter" : "p", "count": 0}, "1001100110101010": { "letter" : "P", "count": 0}, "1001010110101001": { "letter" : "q", "count": 0}, "1001100110101001": { "letter" : "Q", "count": 0}, "1001010110100110": { "letter" : "r", "count": 0}, "1001100110100110": { "letter" : "R", "count": 0}, "1001010101101010": { "letter" : "x", "count": 0}, "1010010110101010": { "letter" : "0", "count": 0}, "1010010110101001": { "letter" : "1", "count": 0}, "1010010110100110": { "letter" : "2", "count": 0}, "1010010110100101": { "letter" : "3", "count": 0}, "1010010110011010": { "letter" : "4", "count": 0}, "1010010110011001": { "letter" : "5", "count": 0}, "1010010110010110": { "letter" : "6", "count": 0}, "1010010110010101": { "letter" : "7", "count": 0}, "1010010101101010": { "letter" : "8", "count": 0}, "1010010101101001": { "letter" : "9", "count": 0}}
dict_letters = {"1001101010101001": { "letter" : "A", "count": 0}, "1001011010101001": { "letter" : "a", "count": 0}, "1001011010100110": { "letter" : "b", "count": 0}, "1001101010100110": { "letter" : "B", "count": 0},"1001011010100101": { "letter" : "c", "count": 0}, "1001101010100101": { "letter" : "C", "count": 0},"1001011010011010": { "letter" : "d", "count": 0},"1001101010011010": { "letter" : "D", "count": 0}, "1001011010011001": { "letter" : "e", "count": 0}, "1001101010011001": { "letter" : "E", "count": 0}, "1001011010010110": { "letter" : "f", "count": 0}, "1001101010010110": { "letter" : "F", "count": 0}, "1001011010010101": { "letter" : "g", "count": 0}, "1001101010010101": { "letter" : "G", "count": 0}, "1001011001101010": { "letter" : "h", "count": 0}, "1001101001101010": { "letter" : "H", "count": 0},"1001011001101001": { "letter" : "i", "count": 0}, "1001101001101001": { "letter" : "I", "count": 0}, "1001011001100110": { "letter" : "j", "count": 0}, "1001101001100110": { "letter" : "J", "count": 0}, "1001011001100101": { "letter" : "k", "count": 0}, "1001101001100101": { "letter" : "K", "count": 0}, "1001011001011010": { "letter" : "l", "count": 0}, "1001101001011010": { "letter" : "L", "count": 0}, "1001011001011001": { "letter" : "m", "count": 0}, "1001101001011001": { "letter" : "M", "count": 0}, "1001011001010110": { "letter" : "n", "count": 0}, "1001101001010110": { "letter" : "N", "count": 0}, "1001011001010101": { "letter" : "o", "count": 0}, "1001101001010101": { "letter" : "O", "count": 0}, "1001010110101010": { "letter" : "p", "count": 0}, "1001100110101010": { "letter" : "P", "count": 0}, "1001010110101001": { "letter" : "q", "count": 0}, "1001100110101001": { "letter" : "Q", "count": 0}, "1001010110100110": { "letter" : "r", "count": 0}, "1001100110100110": { "letter" : "R", "count": 0}, "1001010101101010": { "letter" : "x", "count": 0}, "1010010110101010": { "letter" : "0", "count": 0}, "1010010110101001": { "letter" : "1", "count": 0}, "1010010110100110": { "letter" : "2", "count": 0}, "1010010110100101": { "letter" : "3", "count": 0}, "1010010110011010": { "letter" : "4", "count": 0}, "1010010110011001": { "letter" : "5", "count": 0}, "1010010110010110": { "letter" : "6", "count": 0}, "1010010110010101": { "letter" : "7", "count": 0}, "1010010101101010": { "letter" : "8", "count": 0}, "1010010101101001": { "letter" : "9", "count": 0}}

def analyzeDicLetters():
    global dict_letters,dict_letters_zero,bits
    while True:
        dict_count = {}
        for letter in dict_letters.keys():
            key = dict_letters[letter]["letter"]
            value = dict_letters[letter]["count"]
            dict_count[key]=value
        sort_dict = dict(sorted(dict_count.items(), key=lambda item: item[1], reverse=True))
        
        count_last=0
        index=0
        message = []
        for sort_letter in sort_dict.keys():
            if index == 0:
                count_last= sort_dict[sort_letter]
                message.append(sort_letter)
                index += 1
                continue
            
            if sort_dict[sort_letter] == 0:
                continue
            
            diff = count_last/sort_dict[sort_letter]
            if diff <= 4:
                message.append(sort_letter)
        print(sort_dict)        
        print("".join(message))
        
        #Encerando
        dict_letters=dict_letters_zero
        bits=[]
        time.sleep(10)
        
def analyzeBits():
    global bits,dict_letters

    print("Analizing bits")
    while True:
        strBits = "".join(bits)
        
        for letter in dict_letters.keys():
            count = strBits.count(letter)
            dict_letters[letter]["count"]=count
                
        time.sleep(1)
    
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
    ret, th = cv2.threshold(imgBlur,90,255,cv2.THRESH_BINARY) #80

    #cv2.imshow("image", redim)
    cv2.imshow("Threshold Binary", th)
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
            #print(w_bits)
            #print()
            break
    
    
    img2= im[y_image:y_image+h, corte_negro:corte_negro+w_bits]
    #cv2.imshow("image_bin_recortada", img2)
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
        elif(len(num_bin)>2.5*n and len(num_bin)<=3*n):
            binarios_final.append(num_bin[0])
            binarios_final.append("*")
            binarios_final.append(num_bin[0])
        elif(len(num_bin)>3*n):
            binarios_final.append(num_bin[0])
            binarios_final.append("-")
            binarios_final.append("-")
            binarios_final.append(num_bin[0])
    strBin = "".join(binarios_final)    
    bits.insert(id,strBin)
    
    #corte_blanco=0
    #corte_negro=0
    #x=0
    #h=0
    #datos=[]
    


def main():
    global counter,bits
    print("Start VLC!")
    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1024)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 600)
    cap.set(cv2.CAP_PROP_FPS, 25)
    cap.set(cv2.CAP_PROP_ISO_SPEED, 200)
    cap.set(cv2.CAP_PROP_BRIGHTNESS,72) #70
    cap.set(cv2.CAP_PROP_CONTRAST,40)
    #cap.set(cv2.CAP_PROP_AUTO_EXPOSURE,0.52) #52
    cap.set(cv2.CAP_PROP_EXPOSURE,0.52) #52
    
    # cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1024)
    # cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 600)    
    # cap.set(cv2.CAP_PROP_BRIGHTNESS,70)
    # cap.set(cv2.CAP_PROP_AUTO_EXPOSURE,0.52)
    
    #Starting thread to analize bits
    thanalizeBits = threading.Thread(target=analyzeBits)
    thanalizeBits.start()
    
    thanalyzeDicLetters = threading.Thread(target=analyzeDicLetters)
    thanalyzeDicLetters.start()
    
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
        #cv2.imshow('VLC', image)
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
