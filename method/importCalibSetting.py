import logging
from matplotlib.pyplot import switch_backend
import numpy as np
import ast

def run():
    logging.info('START')
    mtx_0 = convertJobMtx(0)
    dist_0 = convertJobDist(0)
    mtx_1 = convertJobMtx(1)
    dist_1 = convertJobDist(1)
    logging.info('DONE')

    # Return in list[numpy.ndarray,numpy.ndarray,numpy.ndarray,numpy.ndarray]
    return [mtx_0,dist_0,mtx_1,dist_1]



def convertJobMtx(switch):
    if switch == 0:
        with open('./log-camera-calibration-setting/mtx_cam0.txt',"r") as f1:
            
            orgText = f1.read()

            orgText = orgText.replace('][','],[')
            # print(orgText) # For testing
            orgText = orgText.replace(' ',',')
            # print(orgText) # for testing

            # Convert str to list
            norList = ast.literal_eval(orgText)

            # print(type(norList)) # for testing
            # print(norList) # for testing

            # Convert list to numpy.ndarray
            afternp=np.array(norList)

            # print(type(afternp)) # for testing
            # print(afternp) # for testing

    if switch == 1:
        with open('./log-camera-calibration-setting/mtx_cam1.txt',"r") as f1:
            
            orgText = f1.read()
            orgText = orgText.replace('][','],[')
            orgText = orgText.replace(' ',',')

            # Convert str to list
            norList = ast.literal_eval(orgText)

            # Convert list to numpy.ndarray
            afternp=np.array(norList)
    
    return afternp

def convertJobDist(switch):
    if switch == 0:
        with open('./log-camera-calibration-setting/dist_cam0.txt',"r") as f1:
                orgText = f1.read()
                orgText = orgText.replace('  ',',')

                # Convert str to list
                norList = ast.literal_eval(orgText)

                # Convert list to numpy.ndarray
                afternp=np.array(norList)
    if switch == 1:
        with open('./log-camera-calibration-setting/dist_cam1.txt',"r") as f1:
                orgText = f1.read()
                orgText = orgText.replace('  ',',')

                # Convert str to list
                norList = ast.literal_eval(orgText)

                # Convert list to numpy.ndarray
                afternp=np.array(norList)


    return afternp

    
#=---=======================
# print(type(convertJobMtx(0)))
# print(convertJobMtx(0))
# print(convertJobMtx(1))
# print(type(convertJobDist(0)))
# print(convertJobDist(0))
# print(convertJobDist(1))

# aa = run()
# print(type(aa))
# print(type(aa[0]))
# print(type(aa[1]))
# print(type(aa[2]))
# print(type(aa[3]))
# aa = run()
# print(aa)