# -*- coding: utf-8 -*-
"""
Created on Sun Jul 24 12:00:21 2022

@author: user
"""

#Import modules
import cv2

face_cascade = cv2.CascadeClassifier('fd.xml')

#Choose Image

img = cv2.imread('image.jpg')

faces = face_cascade.detectMultiScale(img, 1.1, 4)

for (x, y, w, h) in faces: 
  cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
cv2.imwrite("face_detected.png", img) 
print('Successfully saved')