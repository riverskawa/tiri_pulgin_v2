import os
import re
# import moveObj

# all the combination we got ~
# ('1', '2', '3'), 
# ('1', '2', '4'), 
# ('1', '3', '4'), 
# ('2', '3', '4')

# logic flow
# to run < makeFolder > , create < ./area_method > folder
# to run < copyAll > , copy all the freature_point to < ./area_method > and split by camera
# import the return of < getItemsFromRegion > to < combinWork > to have all the combinations of 3pts area
class classAreaMethod:

    def __init__(self) -> None:
        pass

    def getItemsFromRegion(self):

        ls_c0_r1 = []
        ls_c0_r2 = []
        ls_c0_r3 = []
        ls_c0_r4 = []

        ls_c1_r1 = []
        ls_c1_r2 = []
        ls_c1_r3 = []
        ls_c1_r4 = []

        for cam in ['feature_point_0','feature_point_1']:
            for reg in ['region_1','region_2','region_3','region_4']:
                # camera 0
                if cam == 'feature_point_0' and reg == 'region_1':
                    ls_c0_r1=os.listdir('./after_first_filter/feature_point_0/region_1') # this list containing elements with no path, only elements
                if cam == 'feature_point_0' and reg == 'region_2':
                    ls_c0_r2=os.listdir('./after_first_filter/feature_point_0/region_2')
                if cam == 'feature_point_0' and reg == 'region_3':
                    ls_c0_r3=os.listdir('./after_first_filter/feature_point_0/region_3')
                if cam == 'feature_point_0' and reg == 'region_4':
                    ls_c0_r4=os.listdir('./after_first_filter/feature_point_0/region_4')

                # camera 1
                if cam == 'feature_point_1' and reg == 'region_1':
                    ls_c1_r1=os.listdir('./after_first_filter/feature_point_1/region_1')
                if cam == 'feature_point_1' and reg == 'region_2':
                    ls_c1_r2=os.listdir('./after_first_filter/feature_point_1/region_2')
                if cam == 'feature_point_1' and reg == 'region_3':
                    ls_c1_r3=os.listdir('./after_first_filter/feature_point_1/region_3')
                if cam == 'feature_point_1' and reg == 'region_4':
                    ls_c1_r4=os.listdir('./after_first_filter/feature_point_1/region_4')

        # self.ls_c_r =  [[ls_c0_r1,ls_c0_r2,ls_c0_r3,ls_c0_r4],[ls_c1_r1,ls_c1_r2,ls_c1_r3,ls_c1_r4]]

        # get global starting frame of camera_0
        self.ls_g_c0 = self.globalFrame('./feature_point_0/global_frame_number_0.txt')
        # camera_0
        self.ls_c0combin1 = self.combinWork(ls_c0_r1,ls_c0_r2,ls_c0_r3)
        self.ls_c0combin2 = self.combinWork(ls_c0_r1,ls_c0_r2,ls_c0_r4)
        self.ls_c0combin3 = self.combinWork(ls_c0_r1,ls_c0_r3,ls_c0_r4)
        self.ls_c0combin4 = self.combinWork(ls_c0_r2,ls_c0_r3,ls_c0_r4)

        # get global starting frame of camera_1
        self.ls_g_c1 = self.globalFrame('./feature_point_1/global_frame_number_1.txt')
        # camera_1
        self.ls_c1combin1 = self.combinWork(ls_c1_r1,ls_c1_r2,ls_c1_r3)
        self.ls_c1combin2 = self.combinWork(ls_c1_r1,ls_c1_r2,ls_c1_r4)
        self.ls_c1combin3 = self.combinWork(ls_c1_r1,ls_c1_r3,ls_c1_r4)
        self.ls_c1combin4 = self.combinWork(ls_c1_r2,ls_c1_r3,ls_c1_r4)

        # #run calArea for camera 0
        # self.calArea(self.ls_c0combin1)
        # self.calArea(self.ls_c0combin2)
        # self.calArea(self.ls_c0combin3)
        # self.calArea(self.ls_c0combin4)

        #run calArea for camera 1
        self.calArea(self.ls_c1combin1)
        self.calArea(self.ls_c1combin2)
        self.calArea(self.ls_c1combin3)
        self.calArea(self.ls_c1combin4)

    def combinWork(self,ls_a,ls_b,ls_c):
        ls_combin = []
        for item_a in ls_a:
            for item_b in ls_b:
                for item_c in ls_c:
                    ls_combin.append([item_a,item_b,item_c])
        return ls_combin

    def makeFolder(self):

        # if os.path.exists('./area_method') == False:
        #     os.system('mkdir ./area_method')
        # else:
        #     print('./area_method has already exited') 

    # sub folders
        if os.path.exists('./area_method/1') == False:
            os.system('mkdir ./area_method/1')
        else:
            print('./area_method/1 has already exited') 

        if os.path.exists('./area_method/0') == False:
            os.system('mkdir ./area_method/0')
        else:
            print('./area_method/0 has already exited') 

        print('folders for area_method are settled')

    def copyAll(self):
        for cam in ['feature_point_0','feature_point_1']:
            for reg in ['region_1','region_2','region_3','region_4']:
                path_src = './after_first_filter/'+str(cam)+'/'+str(reg)+'/*'
                if cam == 'feature_point_0':
                    os.system('cp '+str(path_src)+' ./area_method/0')
                if cam == 'feature_point_1':
                    os.system('cp '+str(path_src)+' ./area_method/1')

        print('copy is done')

    def globalFrame(self,path_global_frame):
        list_global= []
        with open(path_global_frame) as f1:
            for line in f1.readlines():
                # print(line)    # testing
                # number = [int(temp)for temp in line.split() if temp.isdigit()]
                coor = re.findall("\d+\.\d+", line)    # format:string    [convect from string with dot to float]
                frame = re.findall('\d+',line)
                global_info = (float(coor[0]),float(coor[1]),int(frame[len(frame)-1]))
                list_global.append(global_info)
            return list_global
    
    # input the list of combination from getItemFromRegion()
    def calArea(self,ls_cw): # ls_cw --> list of calcualtion work
        print('calArea is started')
        # intra switch of camera
        cA_cam_switch = 99
        #creat a folder './area_method/DATA' for storing output data
        if os.path.exists('./area_method/DATA') == True:
            print('./area_method/DATA exited <----')
        else:
            os.system('mkdir ./area_method/DATA')
        # auto camrea distinguish
        if (str(ls_cw[0][0]).split('_'))[1] == '0':
            global_list = self.ls_g_c0
            path2use = './area_method/0/'
            cA_cam_switch = 0
        if (str(ls_cw[0][0]).split('_'))[1] == '1':
            global_list = self.ls_g_c1
            path2use = './area_method/1/'
            cA_cam_switch = 1
        
        
        for combin in ls_cw:
            # check coverage
            by_case_starting_frame = []
            by_case_ending_frame = []
            by_case_len = []
            # getting starting and end frame number of A
            combin0 = path2use+str(combin[0])
            with open(combin0) as f1:
                list_pt_a = []
                for line in f1.readlines():
                    # print(line)    # testing
                    # number = [int(temp)for temp in line.split() if temp.isdigit()]
                    coor = re.findall("\d+\.\d+", line)    # format:string    [convect from string with dot to float]
                    list_pt_a.append(coor) # it contains whole coor of point A

            for j in range (0,len(global_list)):
                if float(list_pt_a[0][0]) == float(global_list[j][0]) and float(list_pt_a[0][1]) == float(global_list[j][1]):
                    print('x,y,frame_a: ',global_list[j]) # testing
                    self.a_starting_frame = int(global_list[j][2]) # A starting frame <<--
                    by_case_starting_frame.append(self.a_starting_frame) # @1
                    print('A_starting_frame:',self.a_starting_frame)
                    break
            by_case_len.append(len(list_pt_a)) # length of A
            by_case_ending_frame.append(int(self.a_starting_frame)+int(len(list_pt_a))-1) # ending frame of A

            # getting starting and end frame number of B
            combin1 = path2use+str(combin[1])
            with open(combin1) as f1:
                list_pt_b = []
                for line in f1.readlines():
                    # print(line)    # testing
                    # number = [int(temp)for temp in line.split() if temp.isdigit()]
                    coor = re.findall("\d+\.\d+", line)    # format:string    [convect from string with dot to float]
                    list_pt_b.append(coor) # it contains whole coor of point A

            for j in range (0,len(global_list)):
                if float(list_pt_b[0][0]) == float(global_list[j][0]) and float(list_pt_b[0][1]) == float(global_list[j][1]):
                    print('x,y,frame_b: ',global_list[j]) # testing
                    self.b_starting_frame = int(global_list[j][2]) # B starting frame <<--
                    by_case_starting_frame.append(self.b_starting_frame)
                    print('B_starting_frame:',self.b_starting_frame)
                    break
            by_case_len.append(len(list_pt_b)) # length of B @2
            by_case_ending_frame.append(int(self.b_starting_frame)+int(len(list_pt_b))-1) # ending frame of B

            # getting starting and end frame number of C
            combin2 = path2use+str(combin[2])
            with open(combin2) as f1:
                list_pt_c = []
                for line in f1.readlines():
                    # print(line)    # testing
                    # number = [int(temp)for temp in line.split() if temp.isdigit()]
                    coor = re.findall("\d+\.\d+", line)    # format:string    [convect from string with dot to float]
                    list_pt_c.append(coor) # it contains whole coor of point A

            for j in range (0,len(global_list)):
                if float(list_pt_c[0][0]) == float(global_list[j][0]) and float(list_pt_c[0][1]) == float(global_list[j][1]):
                    print('x,y,frame_c: ',global_list[j]) # testing
                    self.c_starting_frame = int(global_list[j][2]) # C starting frame <<--
                    by_case_starting_frame.append(self.c_starting_frame) # @3
                    print('C_starting_frame:',self.c_starting_frame)
                    break
            by_case_len.append(len(list_pt_c)) # length of C
            by_case_ending_frame.append(int(self.c_starting_frame)+int(len(list_pt_c))-1) # ending frame of C
        
            # do check (to check the common valid range)
            skip_case = 0
            for starting in by_case_starting_frame:
                for ending in by_case_ending_frame:
                    if starting > ending:
                        skip_case = 1
                        break
                if skip_case ==1:
                    break
            
            # 
            if skip_case == 0:
                self.coreWork(by_case_starting_frame,by_case_ending_frame,combin0,combin1,combin2,cA_cam_switch)

    def coreWork(self,ls_start,ls_end,path_coorTxt_0,path_coorTxt_1,path_coorTxt_2,cam_switch):

        ls_coor_0 = []
        ls_coor_1 = []
        ls_coor_2 = []

        common_start = max(ls_start) # get the max starting frame from the combination
        common_end = min(ls_end) # get the min ending frame from the combination

        # each intra frame to count = common_start - each global start
        intra_start_0 = common_start-ls_start[0]
        intra_start_1 = common_start-ls_start[1]
        intra_start_2 = common_start-ls_start[2]

        # get common len
        common_len = common_end-common_start

        with open(path_coorTxt_0) as f1:
            for line in f1.readlines():
                # print(line)    # testing
                # number = [int(temp)for temp in line.split() if temp.isdigit()]
                coor = re.findall("\d+\.\d+", line)    # format:string    [convect from string with dot to float]
                ls_coor_0.append(coor) # it contains whole coor of point A
    
        with open(path_coorTxt_1) as f2:
            for line2 in f2.readlines():
                # print(line)    # testing
                # number = [int(temp)for temp in line.split() if temp.isdigit()]
                coor2 = re.findall("\d+\.\d+", line2)    # format:string    [convect from string with dot to float]
                ls_coor_1.append(coor2) # it contains whole coor of point A

        with open(path_coorTxt_2) as f3:
            for line3 in f3.readlines():
                # print(line)    # testing
                # number = [int(temp)for temp in line.split() if temp.isdigit()]
                coor3 = re.findall("\d+\.\d+", line3)    # format:string    [convect from string with dot to float]
                ls_coor_2.append(coor3) # it contains whole coor of point A

        # calculate for each frame （one combination）
        ls_area_output = []
        #appending case infomations
        ls_area_output.append('camera_id: '+str(cam_switch))
        ls_area_output.append('p0: '+str(path_coorTxt_0))
        ls_area_output.append('p1: '+str(path_coorTxt_1))
        ls_area_output.append('p2: '+str(path_coorTxt_2))
        ls_area_output.append('p0,p1,p2_start Frame:'+str(ls_start))
        ls_area_output.append('p0,p1,p2_len Frame: '+str(len(ls_coor_0))+', '+str(len(ls_coor_1))+', '+str(len(ls_coor_2)))
        ls_area_output.append('p0,p1,p2_end Frame: '+str(ls_end))
        ls_area_output.append('intra_start_0: '+str(intra_start_0))
        ls_area_output.append('intra_start_1: '+str(intra_start_1))
        ls_area_output.append('intra_start_2: '+str(intra_start_2))
        ls_area_output.append('common_start Frame: '+str(common_start))
        ls_area_output.append('common_end Frame: '+str(common_end))
        ls_area_output.append('common_len Frame: '+str(common_len))
        

        for layer_num in range (0,common_len):

            #get x and y coordinates of each point
            p0x=float(ls_coor_0[intra_start_0+layer_num][0])
            p0y=float(ls_coor_0[intra_start_0+layer_num][1])
            p1x=float(ls_coor_1[intra_start_1+layer_num][0])
            p1y=float(ls_coor_1[intra_start_1+layer_num][1])
            p2x=float(ls_coor_2[intra_start_2+layer_num][0])
            p2y=float(ls_coor_2[intra_start_2+layer_num][1])

            #area
            area = 0.5 * abs(p1x * p2y + p0x * p1y + p2x * p0y - p2x * p1y - p1x * p0y - p0x * p2y)
            ls_area_output.append(area)
            print('AREA :',area)
        
        #write data txt
        p0_id = str(str(path_coorTxt_0).split('/')[-1]).replace('_th.txt','') #str
        p1_id = str(str(path_coorTxt_1).split('/')[-1]).replace('_th.txt','') #str
        p2_id = str(str(path_coorTxt_2).split('/')[-1]).replace('_th.txt','') #str
        # set the path under './areaMethod/DATA'
        path_output = './area_method/DATA/c'+str(cam_switch)+'_'+p0_id+'_'+p1_id+'_'+p2_id+'_AREA.txt'
        with open(path_output, 'w') as f:
            for obj in ls_area_output:
                f.write(str(obj)+'\n')
        f.close()

            

#==============================
# makeFolder()
# copyAll()
job =classAreaMethod()
# job.makeFolder()
# job.copyAll()

job.getItemsFromRegion()
# job.calArea()