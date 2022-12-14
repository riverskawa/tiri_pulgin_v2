from genericpath import exists
from os import path
import shutil
import os
import logging


def run(path_target_folder):

    logging.info('START')

    if os.path.exists('./cali-board-0'):
        shutil.move('./cali-board-0',path_target_folder)
        logging.info('folder ./cali-board-0 is moved to: '+str(path_target_folder))
    else:
        logging.info('folder ./cali-board-0 does not exit')

    if os.path.exists('./cali-board-1'):
        shutil.move('./cali-board-1',path_target_folder)
        logging.info('folder ./cali-board-1 is moved to: '+str(path_target_folder))
    else:
        logging.info('folder ./cali-board-1 does not exit')

    if os.path.exists('./dbscan_output'):
        shutil.move('./dbscan_output',path_target_folder)
        logging.info('folder ./dbscan_output is moved to: '+str(path_target_folder))
    else:
        logging.info('folder ./dbscan_output does not exit')

    if os.path.exists('./feature_point_0'):
        shutil.move('./feature_point_0',path_target_folder)
        logging.info('folder ./feature_point_0 is moved to: '+str(path_target_folder))
    else:
        logging.info('folder ./feature_point_0 does not exit')

    if os.path.exists('./feature_point_1'):
        shutil.move('./feature_point_1',path_target_folder)
        logging.info('folder ./feature_point_1 is moved to: '+str(path_target_folder))
    else:
        logging.info('folder ./feature_point_1 does not exit')

    if os.path.exists('./graph'):
        shutil.move('./graph',path_target_folder)
        logging.info('folder ./graph is moved to: '+str(path_target_folder))
    else:
        logging.info('folder ./graph does not exit')

    if os.path.exists('./temp_img_0'):
        shutil.move('./temp_img_0',path_target_folder)
        logging.info('folder ./temp_img_0 is moved to: '+str(path_target_folder))
    else:
        logging.info('folder ./temp_img_0 does not exit')

    if os.path.exists('./temp_img_1'):
        shutil.move('./temp_img_1',path_target_folder)
        logging.info('folder ./temp_img_1 is moved to: '+str(path_target_folder))
    else:
        logging.info('folder ./temp_img_1 does not exit')

    if os.path.exists('./video'):
        shutil.move('./video',path_target_folder)
        logging.info('folder ./video is moved to: '+str(path_target_folder))
    else:
        logging.info('folder ./video does not exit')

    if os.path.exists('./after_first_filter'):
        shutil.move('./after_first_filter',path_target_folder)
        logging.info('folder ./after_first_filter is moved to: '+str(path_target_folder))
    else:
        logging.info('folder ./after_first_filter does not exit')

    if os.path.exists('./displacementPerFrame'):
        shutil.move('./displacementPerFrame',path_target_folder)
        logging.info('folder ./displacementPerFrame is moved to: '+str(path_target_folder))
    else:
        logging.info('folder ./displacementPerFrame does not exit')

    if os.path.exists('./excel_0'):
        shutil.move('./excel_0',path_target_folder)
        logging.info('folder ./excel_0 is moved to: '+str(path_target_folder))
    else:
        logging.info('folder ./excel_0 does not exit')

    if os.path.exists('./excel_1'):
        shutil.move('./excel_1',path_target_folder)
        logging.info('folder ./excel_1 is moved to: '+str(path_target_folder))
    else:
        logging.info('folder ./excel_1 does not exit')

    #pt_diff_txt_0
    if os.path.exists('./pt_diff_txt_0'):
        shutil.move('./pt_diff_txt_0',path_target_folder)
        logging.info('folder ./pt_diff_txt_0 is moved to: '+str(path_target_folder))
    else:
        logging.info('folder ./pt_diff_txt_0 does not exit')

    #pt_diff_txt_1
    if os.path.exists('./pt_diff_txt_1'):
        shutil.move('./pt_diff_txt_1',path_target_folder)
        logging.info('folder ./pt_diff_txt_1 is moved to: '+str(path_target_folder))
    else:
        logging.info('folder ./pt_diff_txt_1 does not exit')