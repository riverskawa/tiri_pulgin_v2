import cv2
import numpy as np
import os
import glob
import logging

def run(address,switch):
    try:
        logging.info(str(address))
        # Defining the dimensions of checkerboard
        CHECKERBOARD =  (6,8)
        criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)

        # Creating vector to store vectors of 3D points for each checkerboard image
        objpoints = []
        # Creating vector to store vectors of 2D points for each checkerboard image
        imgpoints = [] 


        # Defining the world coordinates for 3D points
        objp = np.zeros((1, CHECKERBOARD[0]*CHECKERBOARD[1], 3), np.float32)
        objp[0,:,:2] = np.mgrid[0:CHECKERBOARD[0], 0:CHECKERBOARD[1]].T.reshape(-1, 2)
        prev_img_shape = None

        # Extracting path of individual image stored in a given directory
        if switch == '_0':
            address = str(address)+'/*_0.bmp'
        if switch == '_1':
            address = str(address)+'/*_1.bmp'

        images = glob.glob(address)
        i=0
        for fname in images:
            logging.info(str(fname))
            img = cv2.imread(fname)
            gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            # Find the chess board corners
            # If desired number of corners are found in the image then ret = true
            ret, corners = cv2.findChessboardCorners(gray, CHECKERBOARD, cv2.CALIB_CB_ADAPTIVE_THRESH+
                cv2.CALIB_CB_FAST_CHECK+cv2.CALIB_CB_NORMALIZE_IMAGE)
            
            """
            If desired number of corner are detected,
            we refine the pixel coordinates and display 
            them on the images of checker board
            """
            
            if ret == True:
                objpoints.append(objp)
                # refining pixel coordinates for given 2d points.
                corners2 = cv2.cornerSubPix(gray,corners,(11,11),(-1,-1),criteria)
                
                imgpoints.append(corners2)

                # Draw and display the corners
                img = cv2.drawChessboardCorners(img, CHECKERBOARD, corners2,ret)

            # cv2.imshow('img',img)
            if switch == '_0':
                output_name = './cali-board-0/output'+str(i)+switch+'.jpg'
            if switch == '_1':
                output_name = './cali-board-1/ouput'+str(i)+switch+'.jpg'
            logging.info('imwrite: '+str(output_name))
            cv2.imwrite(output_name,img)

            i+=1


        h,w = img.shape[:2]

        """
        Performing camera calibration by 
        passing the value of known 3D points (objpoints)
        and corresponding pixel coordinates of the 
        detected corners (imgpoints)
        """
        ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(objpoints, imgpoints, gray.shape[::-1],None,None)

        logging.info('Camera matrix : '+str(mtx))
        logging.info('dist : '+str(dist))
        logging.info('rvecs : '+str(rvecs))
        logging.info('tvecs : '+str(tvecs))

        return [mtx,dist,rvecs,tvecs]
    
    except Exception as e:
        logging.error(e)