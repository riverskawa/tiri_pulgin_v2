import cv2
import logging
import glob

# 标定(Full version)
# def remove_distortion(path,cam_id,mtx, dist, rvecs, tvecs):
# 标定
def remove_distortion(path,cam_id,mtx, dist):
    try:
        logging.info('START')
        # 去畸变
        if cam_id == 0:
            path2 = path+'/*_0.bmp'
        if cam_id == 1:
            path2 = path+'/*_1.bmp'

        for img in glob.glob(path2):
            
            img2 = cv2.imread(img)
            h,  w = img2.shape[:2]
            newcameramtx, roi=cv2.getOptimalNewCameraMatrix(mtx,dist,(w,h),0,(w,h)) # 自由比例参数
            dst = cv2.undistort(img2, mtx, dist, None, newcameramtx)

            # 根据前面ROI区域裁剪图片
            #x,y,w,h = roi
            #dst = dst[y:y+h, x:x+w]
            # dst = cv2.resize(dst,(400,400))

            img3 = str(img).replace('\\','/') # Convect all the "\"(format of path from glob) to "/"
            img3= img3.replace(path,'') # Eliminate the part of path of folder, to obtain the name of image only
            logging.info(img3+'  Starts')
            if cam_id == 0:
                img3='./temp_img_0/'+img3 # The path of saving the processed images for camera-0
            if cam_id == 1:
                img3='./temp_img_1/'+img3 # The path of saving the processed images for camera-1

            cv2.imwrite(img3,dst) # Output images
            # end = time.time() - s

            # cv2.imshow('fin',dst)
            # cv2.waitKey()
            # cv2.destroyAllWindows()

            # # 反投影误差
            # total_error = 0
            # for i in range(len(objpoints)):
            #     imgpoints2, _ = cv2.projectPoints(objpoints[i], rvecs[i], tvecs[i], mtx, dist)
            #     error = cv2.norm(imgpoints[i],imgpoints2, cv2.NORM_L2)/len(imgpoints2)
            #     total_error += error
            # logging.info('total error: '+str(total_error/len(objpoints)))

    except Exception as e:
        logging.error(e)
