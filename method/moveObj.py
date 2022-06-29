import glob
import shutil
import logging

def run(glob_input,destination):
    logging.info('START')
    for i in glob.glob(glob_input):
        shutil.move(i,destination)
    logging.info('END')


# run('./*0_th.txt','./pt_diff_0')