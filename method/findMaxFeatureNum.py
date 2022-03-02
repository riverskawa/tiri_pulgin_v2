import os
import glob
import logging


def run(file_glob,switch):
    try:
        if switch == 0:
            logging.info('Case 0')
            file_glob2 = file_glob+'/*.txt'

        if switch == 1:
            logging.info('Case 1')
            file_glob2 = file_glob+'/*.txt'


    #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> 

        # to find out the max frames per video
        max_line = int(0)
        for txt_th in glob.glob(file_glob2):

            txt_th_read = open(txt_th)
            txt_th_read_num = txt_th_read.readlines()
            logging.info('length of txt lines: '+str(len(txt_th_read_num)))

            if len(txt_th_read_num) > max_line:
                max_line = len(txt_th_read_num)
                logging.info('max lines refreshed :'+str(max_line))

    #<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

        logging.info('final max frame number: '+str(max_line))
        return max_line
    
    except Exception as e:
        logging.error(e)