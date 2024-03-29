import os
import logging
import glob
import threading

import method.calibration
import method.imageProcessing
import method.imageProcessing1
import method.imgToVid
import method.opticalFlow
import method.moveObj
import method.findMaxFeatureNum
import method.findFeatureInfo
import method.getImgSize
import method.plot
import method.txtInsert
import method.dbscan
import method.moveFolder
import method.importCalibSetting
import method.importCalibSettingInput
import method.calibSettingRefresh


class interfaceCalibration:
    def __init__(self) -> None:
        try:

            self.list_cam0_param = []
            self.list_cam1_param = []
            pass
        except Exception as e:
            logging.error(e)

    def calib(self,path_folder_cali_img):
        try:
            self.path_folder_cali_img = path_folder_cali_img
            # init job of calibration
            method.calibSettingRefresh.run()

            # Creating a folder to contain the calibration board images
            if os.path.exists('./cali-board-0') != True:
                os.mkdir('./cali-board-0')
                logging.info('mkdir ./cali-board-0')
            else:
                logging.info('the path already exited: ./cali-board-0')

            if os.path.exists('./cali-board-1') !=True:
                os.mkdir('./cali-board-1')
                logging.info('mkdir ./cali-board-1')
            else:
                logging.info('the path already exited: ./cali-board-1')

            # Calculating the internal parameters of cameras
            threading.Thread(target=self.calibCam0).start()
            threading.Thread(target=self.calibCam1).start()
        
        except Exception as e:
            logging.error(e)

    def calibCam0(self):
        self.list_cam0_param = method.calibration.run(self.path_folder_cali_img,'_0') # -->[mtx,dist,rvecs,tvecs]
        method.txtInsert.run(self.list_cam0_param,0)
    def calibCam1(self):
        self.list_cam1_param = method.calibration.run(self.path_folder_cali_img,'_1') # -->[mtx,dist,rvecs,tvecs]
        method.txtInsert.run(self.list_cam1_param,1)

    def skipCalib(self):
        list_skip_calib = method.importCalibSetting.run()
        self.list_cam0_param = [list_skip_calib[0],list_skip_calib[1]]
        self.list_cam1_param = [list_skip_calib[2],list_skip_calib[3]]
    
    def skipCalibInput(self,path):
        list_skip_calib_input = method.importCalibSettingInput.run(path)
        self.list_cam0_param = [list_skip_calib_input[0],list_skip_calib_input[1]]
        self.list_cam1_param = [list_skip_calib_input[2],list_skip_calib_input[3]]

    def imgProc(self,path_folder_proc_img):
        try:
            self.path_folder_proc_img = path_folder_proc_img
            # Creating a folder to contain the operation images
            if os.path.exists('./temp_img_0') != True:
                os.mkdir('./temp_img_0')
                logging.info('mkdir ./temp_img_0')
            else:
                logging.info('the path already exited: ./temp_img_0')
            
            if os.path.exists('./temp_img_1') != True:
                os.mkdir('./temp_img_1')
                logging.info('mkdir ./temp_img_1')
            else:
                logging.info('the path already exited: ./temp_img_1') 

            # Undergoing image processing
            self.imgProcCam0()

        except Exception as e:
            logging.error(e)

    def imgProcCam0(self):
        method.imageProcessing.remove_distortion(self.path_folder_proc_img,0,self.list_cam0_param[0],self.list_cam0_param[1])
        method.imageProcessing1.remove_distortion(self.path_folder_proc_img,1,self.list_cam1_param[0],self.list_cam1_param[1])





class interfaceImgToVid:

    def __init__(self) -> None:
        try:
            if os.path.exists('./video') != True:
                os.mkdir('./video')
                logging.info('mkdir ./video')
            else:
                logging.info('the path already exited: ./video')
            pass

        except Exception as e:
            logging.error(e)

    def doTransfer(self):
        try:
            method.imgToVid.cam0()
            method.imgToVid.cam1()
            method.moveObj.run('./*.avi','./video')
        except Exception as e:
            logging.error(e)



class interfaceOpticalFlow:

    def __init__(self) -> None:
        try:
            pass
        except Exception as e:
            logging.error(e)

    def doOpticalFlow(self):
        try:
            method.opticalFlow.App('./video/cam_0.avi',0).run() # Folder(# Folder(./feature_point_0) is created) is created
            method.opticalFlow.App('./video/cam_1.avi',1).run() # Folder(./feature_point_1) is created
            
            method.moveObj.run('./*_0_th.txt','./feature_point_0/')
            method.moveObj.run('./*_1_th.txt','./feature_point_1/')

        except Exception as e:
            logging.error(e)
        

class interfaceCalulation:

    def __init__(self) -> None:
        try:
            pass

        except Exception as e:
            logging.error(e)
    

    def doCal(self):
        try:

            self.gen_img_size = method.getImgSize.run('./temp_img_0')
            self.max_frame_num_0 = method.findMaxFeatureNum.run('./feature_point_0/',0)
            self.max_frame_num_1 = method.findMaxFeatureNum.run('./feature_point_1/',1)

            method.findFeatureInfo.run('./feature_point_0/',self.max_frame_num_0,0,self.gen_img_size[0]) # No return
            method.findFeatureInfo.run('./feature_point_1/',self.max_frame_num_1,1,self.gen_img_size[0]) # No return

            return [self.max_frame_num_0,self.max_frame_num_1]


        except Exception as e:
            logging.error(e)


class interfaceDBScan:

    def __init__(self) -> None:
        pass

    def doDBScan(self,max_frame_0,max_frame_1):
        try:
            if os.path.exists('./dbscan_output') != True:
                os.mkdir('./dbscan_output')
                logging.info('mkdir ./dbscan_output')
            else:
                logging.info('path has already exited ./dbscan_output')
            
            method.dbscan.run(0,int(max_frame_0))
            method.dbscan.run(1,int(max_frame_1))


        
        except Exception as e:
            logging.error(e)

class interfaceMoveFolder:
    def __init__(self) -> None:
        pass

    def doMoveFolder(self,target_folder):
        try:
            method.moveFolder.run(target_folder)

        except Exception as e:
            logging.error(e)
        
