# -*- coding: utf-8 -*-
"""
Created on Fri Nov  1 21:22:50 2019

@author: Emine
"""


import numpy as np
import cv2

def opening(image,se):
    image_erode = erosion(image,se)
    image_dilate =  dilation(image_erode,se)
    return image_dilate
    
def closing(image,se):
    image_dilate =  dilation(image,se)
    image_erode = erosion(image_dilate,se)
    return image_erode

def dilation(padded_image,se):
    image_h, image_w = padded_image.shape
  
    
    image_conv = np.zeros((image_h,image_w))
    for i in range(image_h-1):
        for j in range(image_w-1):
            if(padded_image[i][j] ==  se[1][1] or padded_image[i-1][j-1] ==  se[0][0] or padded_image[i][j-1] ==  se[1][0] or padded_image[i-1][j] ==  se[0][1] or padded_image[i][j+1] ==  se[1][2] or padded_image[i+1][j+1] ==  se[2][2] or padded_image[i+1][j] ==  se[2][1] or padded_image[i+1][j-1] ==  se[2][0] or padded_image[i-1][j+1] ==  se[0][2] != 0): #center(1,1)
               image_conv[i][j] = se[1][1]
              
                                         
                
    return image_conv
    
def erosion(padded_image,se):
    image_h,image_w  = padded_image.shape
   
   
    image_conv = np.zeros((image_h,image_w))
    for i in range(image_h-1):
        for j in range(image_w-1):
            if(padded_image[i][j] ==  se[1][1] and padded_image[i-1][j-1] ==  se[0][0] and padded_image[i][j-1] ==  se[1][0] and padded_image[i-1][j] ==  se[0][1] and padded_image[i][j+1] ==  se[1][2] and padded_image[i+1][j+1] ==  se[2][2] and padded_image[i+1][j] ==  se[2][1] and padded_image[i+1][j-1] ==  se[2][0] and padded_image[i-1][j+1] ==  se[0][2] != 0): #center(1,1)
                image_conv[i][j] =  se[1][1]
                
    return image_conv
    
    
    
    
se = np.array([[255,255,255],[255,255,255],[255,255,255]],dtype=np.uint8) #square structural element
img=cv2.imread('fingerprint.tif')
red,green,blue = cv2.split(img)


padded_image = cv2.copyMakeBorder(img,1,1,1,1,cv2.BORDER_CONSTANT,value=0)#zero-padding
red_opened = opening(red,se)
green_opened = opening(green,se)
blue_opened = opening(blue,se)

red_closed = closing(red_opened,se)
green_closed = closing(green_opened,se)
blue_closed = closing(blue_opened,se)

image_opened = np.delete(cv2.merge((red_opened,green_opened,blue_opened)),0 and 239,0)#Standardization image sizes to input image size
image_closed = np.delete(cv2.merge((red_closed,green_closed,blue_closed)),0 and 316,1)

cv2.imshow("opening",image_opened)
cv2.imshow("closing",image_closed)
cv2.imshow("original",padded_image)



cv2.waitKey(0)
cv2.destroyAllWindows()


