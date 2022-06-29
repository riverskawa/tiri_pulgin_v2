
import os
import logging
import shutil

'''for scanning and removing folder'''

def run():
    if os.path.exists('./cali-board-0') != True:
        logging.info('folder does not exit: ./cali-board-0')
    else:
        shutil.rmtree('./cali-board-0')
        logging.info('folder is deleted: ./cali-board-0')

    if os.path.exists('./cali-board-1') != True:
        logging.info('folder does not exit: ./cali-board-1')
    else:
        shutil.rmtree('./cali-board-1')
        logging.info('folder is deleted: ./cali-board-1')

    if os.path.exists('./graph') != True:
        logging.info('folder does not exit: ./graph')
    else:
        shutil.rmtree('./graph')
        logging.info('folder is deleted: ./graph')

    # if os.path.exists('./log-camera-calibration-setting') != True:
    #     logging.info('folder does not exit: ./log-camera-calibration-setting')
    # else:
    #     shutil.rmtree('./log-camera-calibration-setting')
    #     logging.info('folder is deleted: ./log-camera-calibration-setting')

    if os.path.exists('./temp_img_0') != True:
        logging.info('folder does not exit: ./temp_img_0')
    else:
        shutil.rmtree('./temp_img_0')
        logging.info('folder is deleted: ./temp_img_0')

    if os.path.exists('./temp_img_1') != True:
        logging.info('folder does not exit: ./temp_img_1')
    else:
        shutil.rmtree('./temp_img_1')
        logging.info('folder is deleted: ./temp_img_1')

    if os.path.exists('./video') != True:
        logging.info('folder does not exit: ./video')
    else:
        shutil.rmtree('./video')
        logging.info('folder is deleted: ./video')

    if os.path.exists('./feature_point_0') != True:
        logging.info('folder does not exit: ./feature_point_0')
    else:
        shutil.rmtree('./feature_point_0')
        logging.info('folder is deleted: ./feature_point_0')

    if os.path.exists('./feature_point_1') != True:
        logging.info('folder does not exit: ./feature_point_1')
    else:
        shutil.rmtree('./feature_point_1')
        logging.info('folder is deleted: ./feature_point_1')

    if os.path.exists('./dbscan_output') != True:
        logging.info('folder does not exit: ./dbscan_output')
    else:
        shutil.rmtree('./dbscan_output')
        logging.info('folder is deleted: ./dbscan_output')

    if os.path.exists('./after_first_filter') != True:
        logging.info('folder does not exit: ./after_first_filter')
    else:
        shutil.rmtree('./after_first_filter')
        logging.info('folder is deleted: ./after_first_filter')

    if os.path.exists('./pt_diff_0') != True:
        logging.info('folder does not exit: ./pt_diff_0')
    else:
        shutil.rmtree('./pt_diff_0')
        logging.info('folder is deleted: ./pt_diff_0')

    if os.path.exists('./pt_diff_1') != True:
        logging.info('folder does not exit: ./pt_diff_1')
    else:
        shutil.rmtree('./pt_diff_1')
        logging.info('folder is deleted: ./pt_diff_1')