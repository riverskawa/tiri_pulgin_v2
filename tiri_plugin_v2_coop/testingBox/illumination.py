import cv2
import numpy as np


def illum(imgg):
    img = cv2.imread(imgg)
    img_bw = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    thresh = cv2.threshold(img_bw,180,255,0)[1]

    cnts = cv2.findContours(thresh.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)[0]
    img_zero = np.zeros(img.shape,dtype=np.uint8)

    for cnt in cnts:
        x, y, w, h = cv2.boundingRect(cnt)
        img_zero[y:y+h,x:x+w] = 255

        mask = img_zero

    result = cv2.illuminationChange(img,mask,alpha=0.2,beta=0.4)
    cv2.imwrite('tst.png',result)
    #return result


illum('./testingBox/reflection.png')