import picamera
import time
import cv2
import numpy as np
import tkinter


"""scaling_factor = 5
width = 2592
height = 1952
#initialize roi as one single column:
roi = int(width/2)#column of interest TODO: expand ROI to [x,y,w,h]"""

path = "/media/danielsg27/0C78-D0E6/Pruebas_OCC/Capturas/"
path_RBin = "/media/danielsg27/0C78-D0E6/Pruebas_OCC/Capturas/Capturas_ROI/"
# ROI = x,y w,h
x = 200
y = 120
w = 100
h = 780

kernel = np.ones((5, 5), np.uint8)

with picamera.PiCamera() as camera:
    camera.rotation = -90
    camera.ISO = 800
    camera.resolution=(1024,600)
    camera.shutter_speed = 150 #100 o 180
    camera.brightness = 85 # 75
    camera.contrast = 100
    for i in range (10):
        time.sleep(0.2) # 200ms
        camera.capture(path + 'IMG_%04d.jpg' % i)
    camera.stop_preview()
    camera.close()
