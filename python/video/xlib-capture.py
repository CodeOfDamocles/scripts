'''                                                                                  
Records desktop frame buffer on Linux desktops                                       
and converts data into openCV useable format                                         
'''                                                                                  
from Xlib import display, X                                                          
from PIL import Image                                                                
import cv2                                                                           
import numpy as np                                                                   
                                                                                     
W,H = 800,800                                                                        
dsp = display.Display()                                                              
root = dsp.screen().root                                                             
                                                                                     
while 1:                                                                             
    raw = root.get_image(0, 0, W,H, X.ZPixmap, 0xffffffff)                           
    image = Image.frombytes("RGB", (W, H), raw.data, "raw", "BGRX")                  
    img = np.array(image)                                                            
    cv2.imshow('window',img)                                                         
    cv2.waitKey(100)  
