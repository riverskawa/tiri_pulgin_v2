import glob
import shutil
import logging

def run(glob_input,destination):
    logging.info('START')
    for i in glob.glob(glob_input):
        shutil.move(i,destination)
    logging.info('END')

# run('./*_0_th.txt','./pt_diff_txt_0')
# run('./*_0_th.xlsx','./excel_0')
# run('./*_1_th.txt','./pt_diff_txt_1')
# run('./*_1_th.xlsx','./excel_1')