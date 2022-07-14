import os
import shutil
import logging
import glob
import datetime
from sys import path

def run():
    logging.info('START')
    # Check the './log-camera-calibration-setting-OLD' has exited or not
    if os.path.exists:
        logging.info('the path has exited: ./log-camera-calibration-setting-OLD')
    else:
        os.mkdir('./log-camera-calibration-setting-OLD')
        logging.info('mkdir ./log-camera-calibration-setting-OLD')

    # Move the old version of camera calibration setting

    for obj in glob.glob('./log-camera-calibration-setting/*.txt'):
        obj_src = str(obj).replace('\\','/')
        # Start to rename
        obj_dst = obj_src.replace('.txt','')


        date_time_str = str(datetime.datetime.today())
        date_time_str = date_time_str.replace(' ','_')
        date_time_str = date_time_str.replace(':','-')
        date_time_str = date_time_str.replace('.','-')

        obj_dst = obj_dst+'_DEACTIVATE-TIME:_'+date_time_str+'.txt'

        file_old_name = os.path.join(obj_src)
        file_new_name = os.path.join(obj_dst)
        os.rename(file_old_name,file_new_name)
        shutil.move(obj_dst,'./log-camera-calibration-setting-OLD')

    logging.info('END')
