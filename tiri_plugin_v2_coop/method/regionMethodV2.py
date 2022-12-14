import glob
import logging
import re
from itertools import combinations
import math
import cv2
import os


from openpyxl.drawing.image import Image

from  openpyxl import Workbook, load_workbook
from datetime import datetime
from openpyxl.chart import (
    ScatterChart,
    Reference,
    Series,
)


class regMethod:
    def __init__(self,cam_num) -> None:
        
        if cam_num == 0:
            self.path_folder_coord = './after_first_filter/feature_point_0'
            self.path_folder_base = './after_first_filter/feature_point_0/region_2'
            self.path_global_frame = './feature_point_0/global_frame_number_0.txt'

            #create excel folder for cam_0
            if os.path.exists('./excel_cam_0'):
                logging.info('./excel_cam_0 has been created')
            else:
                os.system('mkdir ./excel_cam_0')
            self.path_excel = './excel_cam_0'

        if cam_num == 1:
            self.path_folder_coord = './after_first_filter/feature_point_1'
            self.path_folder_base = './after_first_filter/feature_point_1/region_2'
            self.path_global_frame = './feature_point_1/global_frame_number_1.txt'

            #create excel folder for cam_1
            if os.path.exists('./excel_cam_1'):
                logging.info('./excel_cam_1 has been created')
            else:
                os.system('mkdir ./excel_cam_1')
            self.path_excel = './excel_cam_1'
    
        pass

    def catchR2(self):

        golb_path_coord = self.path_folder_base+'/*.txt'

        self.list_global=[]
        self.getGlobalFrame()

        for txt in glob.glob(golb_path_coord):
            path_txt = txt
            txt_name = str(txt).split('/')[-1]
            name = txt_name.replace('.txt','')
            
            # writexlsx(path_txt, self.list_global,name,self.path_excel, self.path_folder_coord).insertR2Data()
            txt_work = txtversion(path_txt, self.list_global,name,self.path_excel, self.path_folder_coord)
            txt_work.get_base()
            txt_work.get_case()

    def getGlobalFrame(self):
        with open(self.path_global_frame) as f1:
            for line in f1.readlines():
                # print(line)    # testing
                # number = [int(temp)for temp in line.split() if temp.isdigit()]
                coor = re.findall("\d+\.\d+", line)    # format:string    [convect from string with dot to float]
                frame = re.findall('\d+',line)
                global_info = (float(coor[0]),float(coor[1]),int(frame[len(frame)-1]))
                self.list_global.append(global_info)


class txtversion:
    def __init__(self,path_base_txt,list_global_1f,base_txt_name,path_save,path_case_folder) -> None:
        self.this_list_global = list_global_1f
        self.this_path_base_txt = path_base_txt
        self.this_base_txt_name = base_txt_name
        self.this_path2save = path_save
        self.this_path_case_folder = path_case_folder
        pass

    def get_base(self):
        #get BASE coord to list
        list_base = []
        with open(self.this_path_base_txt) as f1:
            for line in f1.readlines():
                # print(line)    # testing
                # number = [int(temp)for temp in line.split() if temp.isdigit()]
                coor = re.findall("\d+\.\d+", line)    # format:string    [convect from string with dot to float]
                list_base.append(coor) # it contains whole coor of point BASE
            self.len_base = len(list_base)
            self.ls_base = list_base

        # get BASE global frame
        for i in range (len(self.this_list_global)):
            if float(list_base[0][0]) == float(self.this_list_global[i][0]) and float(list_base[0][1]) == float(self.this_list_global[i][1]):
                logging.info('x,y,frame_base: ',self.this_list_global[i]) # testing
                self.base_starting_frame = int(self.this_list_global[i][2]) # getting the starting frame number of BASE
                logging.info('base_starting_frame:',self.base_starting_frame) 
                break

    def get_case(self):
        #get CASE coord to list
        for reg in (['region_1','region_3','region_4']):
            #create region folder
            if os.path.exists(self.this_path2save+'/'+reg)==False:
                os.system('mkdir '+self.this_path2save+'/'+reg)

            path_region_txt = self.this_path_case_folder+'/'+reg
            for case in glob.glob(path_region_txt+'/*.txt'):
                list_case = []
                with open(case) as f1:
                    for line in f1.readlines():
                        coor = re.findall("\d+\.\d+", line)    # format:string    [convect from string with dot to float]
                        list_case.append(coor) # it contains whole coor of point BASE

                # get CASE global frame
                for i in range (len(self.this_list_global)):
                    if float(list_case[0][0]) == float(self.this_list_global[i][0]) and float(list_case[0][1]) == float(self.this_list_global[i][1]):
                        logging.info('x,y,frame_base: ',self.this_list_global[i]) # testing
                        self.case_starting_frame = int(self.this_list_global[i][2]) # getting the starting frame number of BASE
                        logging.info('base_starting_frame:',self.case_starting_frame) 
                        break
                
                # we got length of base
                # we got starting frame of base
                # get cal_starting_frame
                if self.base_starting_frame > self.case_starting_frame:
                    cal_starting_frame = self.base_starting_frame
                    #get cal-base_len and cal_case_len
                    cal_base_len = self.len_base-(abs(self.base_starting_frame-cal_starting_frame))
                    cal_case_len = len(list_case)-(abs(cal_starting_frame-self.case_starting_frame))
                if self.base_starting_frame == self.case_starting_frame:
                    cal_starting_frame = self.base_starting_frame
                    #get cal-base_len and cal_case_len
                    cal_base_len = self.len_base-(abs(self.base_starting_frame-cal_starting_frame))
                    cal_case_len = len(list_case)-(abs(self.case_starting_frame-cal_starting_frame))
                if self.base_starting_frame < self.case_starting_frame:
                    cal_starting_frame = self.case_starting_frame
                    #get cal-base_len and cal_case_len
                    cal_base_len = self.len_base-(abs(self.base_starting_frame-cal_starting_frame))
                    cal_case_len = len(list_case)-(abs(self.case_starting_frame-cal_starting_frame))
                # #get cal-base_len and cal_case_len
                # cal_base_len = self.len_base-(self.base_starting_frame-cal_starting_frame)
                # cal_case_len = len(list_case)-(self.case_starting_frame-cal_starting_frame)
                if cal_case_len >=1:
                    #get cal_len
                    if cal_base_len > cal_case_len:
                        cal_len = cal_case_len
                    if cal_base_len == cal_case_len:
                        cal_len = cal_base_len               
                    if cal_base_len < cal_case_len:
                        cal_len = cal_base_len
                    #do displacement cal
                    ls_disp = []
                    for disp_term in range(1,cal_len):
                        #x-dircetion
                        x_base = self.ls_base[(cal_starting_frame-self.base_starting_frame)+disp_term-1][0]
                        x_case = list_case[(cal_starting_frame-self.case_starting_frame)+disp_term-1][0]
                        #y-dircetion
                        y_base = self.ls_base[(cal_starting_frame-self.base_starting_frame)+disp_term-1][1]
                        y_case = list_case[(cal_starting_frame-self.case_starting_frame)+disp_term-1][1]

                        x_disp = float(x_base)-float(x_case)
                        y_disp = float(y_base)-float(y_case)
                        disp = math.sqrt((x_disp*x_disp)+(y_disp*y_disp))
                        ls_disp.append(disp)
                    
                    #we got the self.this_base_txt_name --> base name
                    case = str(case).replace(path_region_txt+'/','')
                    case = case.replace('.txt','')
                    txt_output_path = self.this_path2save+'/'+reg+'/'+self.this_base_txt_name+'_'+case+'_'+str(cal_starting_frame)+'.txt'
                    f = open(txt_output_path, 'w')
                    for i in (ls_disp):
                        f.write(str(i)+'\n')
                    f.close()

#==============================
# job=regMethod(1)
# job.catchR2()

