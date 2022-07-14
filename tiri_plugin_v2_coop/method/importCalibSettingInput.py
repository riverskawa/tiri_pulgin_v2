import logging
import numpy as np
import ast

def run(path):
    print(path) # testing
    logging.info('START')
    mtx_0 = convertJobMtx(0,path)
    dist_0 = convertJobDist(0,path)
    mtx_1 = convertJobMtx(1,path)
    dist_1 = convertJobDist(1,path)
    logging.info('DONE')

    # Return in list[numpy.ndarray,numpy.ndarray,numpy.ndarray,numpy.ndarray]
    return [mtx_0,dist_0,mtx_1,dist_1]



def convertJobMtx(switch,path):
    if switch == 0:
        src_file = path+'/mtx_cam0.txt'
        with open(src_file,"r") as f1:
            
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
        src_file = path+'/mtx_cam1.txt'
        with open(src_file,"r") as f1:
            
            orgText = f1.read()
            orgText = orgText.replace('][','],[')
            orgText = orgText.replace(' ',',')

            # Convert str to list
            norList = ast.literal_eval(orgText)

            # Convert list to numpy.ndarray
            afternp=np.array(norList)
    
    return afternp

def convertJobDist(switch,path):
    if switch == 0:
        src_file = path+'/dist_cam0.txt'
        with open(src_file,"r") as f1:
                orgText = f1.read()
                orgText = orgText.replace('  ',',')

                # Convert str to list
                norList = ast.literal_eval(orgText)

                # Convert list to numpy.ndarray
                afternp=np.array(norList)
    if switch == 1:
        src_file = path+'/dist_cam1.txt'
        with open(src_file,"r") as f1:
                orgText = f1.read()
                orgText = orgText.replace('  ',',')

                # Convert str to list
                norList = ast.literal_eval(orgText)

                # Convert list to numpy.ndarray
                afternp=np.array(norList)


    return afternp

    
#=---=======================
