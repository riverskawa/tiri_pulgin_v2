import os
import logging

def run(list,switch):
    try:
        # Creating a folder ./log-camera-calibration-setting
        if os.path.exists('./log-camera-calibration-setting') != True:
            os.mkdir('./log-camera-calibration-setting')
            logging.info('mkdir ./log-camera-calibration-setting')
        else:
            logging.info('path has already exited ./log-camera-calibration-setting')

        #
        if switch == 0:
            mtx_log_path = './log-camera-calibration-setting/mtx_cam0.txt'
            dist_log_path = './log-camera-calibration-setting/dist_cam0.txt'
            rvecs_log_path = './log-camera-calibration-setting/rvecs_cam0.txt'
            tvecs_log_path = './log-camera-calibration-setting/tvecs_cam0.txt'
        if switch == 1:
            mtx_log_path = './log-camera-calibration-setting/mtx_cam1.txt'
            dist_log_path = './log-camera-calibration-setting/dist_cam1.txt'
            rvecs_log_path = './log-camera-calibration-setting/rvecs_cam1.txt'
            tvecs_log_path = './log-camera-calibration-setting/tvecs_cam1.txt'


        with open(mtx_log_path, "w", encoding="utf-8") as f2:
            f2.write(str(list[0]))
        with open(dist_log_path, "w", encoding="utf-8") as f3:
            f3.write(str(list[1]))
        with open(rvecs_log_path, "w", encoding="utf-8") as f4:
            f4.write(str(list[2]))
        with open(tvecs_log_path, "w", encoding="utf-8") as f5:
            f5.write(str(list[3]))

    except Exception as e:
        logging.error(e)


#[mtx,dist,rvecs,tvecs]