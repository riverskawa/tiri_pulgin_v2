import cv2
import numpy as np
import logging
import glob

def run(img_src):
    try:
        img_src_following = str(img_src)+'/*_0.bmp'
 
        img = cv2.imread(glob.glob(img_src_following)[0])
        spec_img = img.shape
        logging.info('Img (row,col): '+str(spec_img[0])+'\t'+str(spec_img[1]))    
        return [spec_img[0],spec_img[1]]

    except Exception as e:
        logging.error(e)