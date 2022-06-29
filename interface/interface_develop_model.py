import os
import logging
import glob
import threading
import re


import method.calibration
import method.imageProcessing
import method.imageProcessing1
import method.imgToVid
import method.opticalFlow
import method.moveObj
import method.findMaxFeatureNum
import method.findFeatureInfo
import method.find_feature_info_for_all
import method.getImgSize
import method.plot
import method.txtInsert
import method.dbscan
import method.moveFolder
import method.markFeature
import method.importCalibSetting
import method.importCalibSettingInput
import method.calibSettingRefresh
import method.FirstFilter
import method.initialization
import method.LineMethod
import method.plot_lineMethod


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
            method.moveObj.run('./*global_frame_number_0.txt','./feature_point_0/')
            method.moveObj.run('./*_1_th.txt','./feature_point_1/')
            method.moveObj.run('./*global_frame_number_1.txt','./feature_point_1/')
            

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

class interfaceCalulation_for_all:

    def __init__(self) -> None:
        try:
            pass

        except Exception as e:
            logging.error(e)
    

    def doCal(self):
        try:

            self.gen_img_size = method.getImgSize.run('./temp_img_0')

            method.find_feature_info_for_all.run('./feature_point_0/',0,self.gen_img_size[0]) # No return
            method.find_feature_info_for_all.run('./feature_point_1/',1,self.gen_img_size[0]) # No return

        except Exception as e:
            logging.error(e)

class interfaceFilter:
    def __init__(self) -> None:
        pass

    def doFilter(self):
        try:
            method.FirstFilter.firstFilter().run(0)
            method.FirstFilter.firstFilter().run(1)
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
        
class interfaceMakeFeatures:
    def __init__(self) -> None:
        pass

    def job_img(self,switch):
        list_img = []
        if switch == 1:
            for img in glob.glob('./temp_img_1/*_1.bmp'):
                img = str(img).replace('\\','/')
                img= img.replace('./temp_img_1/','')
                img=img.replace('C_1.bmp','')
                list_img.append(img)
            list_img.sort()
            target_img = list_img[0]
            target_img = './temp_img_1/'+str(target_img)+'C_1.bmp'
            return target_img
        
        if switch == 0:
            for img in glob.glob('./temp_img_0/*_0.bmp'):
                img = str(img).replace('\\','/')
                img= img.replace('./temp_img_0/','')
                img=img.replace('C_0.bmp','')
                list_img.append(img)
            list_img.sort()
            target_img = list_img[0]
            target_img = './temp_img_0/'+str(target_img)+'C_0.bmp'
            return target_img

    def run(self):

        img_0=self.job_img(0)
        img_1=self.job_img(1)

        for  txt_name in glob.glob('./feature_point_0/*.txt'):
            txt_name = txt_name.replace('\\','/')
            with open(txt_name) as f:
                data = f.readlines()[0]
                data_num = re.findall("\d+\.\d+", data)
                
                float_c = float(data_num[0])
                float_r = float(data_num[1])
            
                method.markFeature.plot_scale()

class interfaceLineMethod:
    def __init__(self) -> None:
        pass

    def run(self):
        try:
            job_a = method.LineMethod.lineMethod(0)
            job_a.globalFrame()
            job_a.getPtsComb()
            job_a.run()
            if os.path.exists('./pt_diff_0'):
                logging.info('./pt_difff_0 has already exited')
            else:
                logging.info('./pt_diff_0 is created')
                os.mkdir('./pt_diff_0')
            method.moveObj.run('./*_0_th.txt','./pt_diff_0')
            
            job_b = method.LineMethod.lineMethod(1)
            job_b.globalFrame()
            job_b.getPtsComb()
            job_b.run()
            if os.path.exists('./pt_diff_1'):
                logging.info('./pt_difff_1 has already exited')
            else:
                logging.info('./pt_diff_1 is created')
                os.mkdir('./pt_diff_1')
            method.moveObj.run('./*_1_th.txt','./pt_diff_1')

            # plot graph
            if os.path.exists('./graph_pt_diff_0'):
                logging.info('./graph_pt_difff_0 has already exited')
            else:
                logging.info('./graph_pt_diff_0 is created')
                os.mkdir('./graph_pt_diff_0')
            # method.plot_lineMethod.plot()


        except Exception as e:
            logging.debug(e)
    #=========================================================================
def run_test():
    method.initialization.run()
    processA = interfaceCalibration()
    processA.skipCalib()
    processA.imgProc('C:/Users/user/Documents/RQQ/t_v2/006_0.025mg_ml_001')
    interfaceImgToVid().doTransfer()
    interfaceOpticalFlow().doOpticalFlow()
    interfaceCalulation_for_all().doCal()
    # interfaceFilter().doFilter()
    # period function ADD HERE
    # interfaceLineMethod().run()
