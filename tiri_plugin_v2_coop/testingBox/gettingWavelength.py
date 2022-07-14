
import re
import matplotlib.pyplot as plt
import glob
import math
import os
import csv


class gettingWavelength:

    def __init__(self) -> None:
        pass

    def run(self):

        # # folder
        # if os.path.exists('./27perGroup_disp'):
        #     print('FOLDER ./27perGroup_disp has already exited')
        # else:
        #     os.mkdir('./27perGroup_disp')
        #     print('FOLDER ./27perGroup_disp has been created')


        plt.switch_backend('agg')

        folder_path ='./displacementPerFrame/*.txt'


        for txt_path in glob.glob(folder_path):
            
            i2 = str(txt_path).replace('\\','/')

            list_disp =[]
            with open(i2, "r") as f1:
                for line in f1.readlines():

                    # number = [int(temp)for temp in line.split() if temp.isdigit()]
                    number = re.findall("\d+\.\d+", line)    # format:string    [convect from string with dot to float]
                    list_disp.append(number)
        listPeak = self.findingPeak(list_disp)
        wavelength = self.getWavelength(listPeak)
        print('normal wavelength:',wavelength)
        return wavelength


    def findingPeak(self,listDisp):
        list_peak = []
        for i in range (0,len(listDisp)):
            if i >= 2 and i <= len(listDisp) - 2:
                if listDisp[i-2] < listDisp[i-1] and listDisp[i-1] < listDisp[i] and listDisp[i] > listDisp[i+1] and listDisp[i+1] > listDisp[i+2]:
                    list_peak.append(i)
        
        print(list_peak)
        return list_peak
        

    def getWavelength(self,listPeak):
        list_gap = []
        list_gap_only = []
        for i in range (0,len(listPeak)):
            if i < len(listPeak)-1:
                gap = listPeak[i+1]-listPeak[i]
                one_gap = [listPeak[i],listPeak[i+1],gap]
                list_gap.append(one_gap)
                list_gap_only.append(gap)
        
        set_gap_only = set(list_gap_only)
        list_wavelength = []
        for item in set_gap_only:
            list_wavelength.append([item,list_gap_only.count(item)])
        max_item_num = 0
        index_max_item_num = 0
        for i in range (0,len(list_wavelength)):
            if list_wavelength[i][1] >= max_item_num:
                max_item_num=list_wavelength[i][1]
                index_max_item_num = i
        print('[wavelength,frequency]: ',list_wavelength[index_max_item_num])
        return int(list_wavelength[index_max_item_num][0])

# TESTING==================================
# twentysevenpergroup().writeTxt()
# twentysevenpergroup().run()
gettingWavelength().run()