path='/home/taju/Downloads/images.png'
import cv2
import numpy as np


def write_text(list ,limit_temp):
    img = np.ones([159, 318, 3])*255
    off = int(318/(len(list)))
    x,y =0 ,50

    for index ,word in enumerate(list):
        cv2.putText(img, str(word), (x, y + off * index), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
    # cv2.imshow('frame', img)
    return img
    # cv2.waitKey(5000)
list= ['Tejal Gole' , 'Spo = 98', 'Temp =27.6']
input_frame=cv2.imread(path)
new_img =write_text(list,limit_temp=0)
output_frame = np.concatenate((input_frame, new_img), 1)
cv2.imshow('frame', output_frame)
cv2.waitKey(5000)