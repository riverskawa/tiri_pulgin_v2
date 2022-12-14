import os

def run_pack(case_name):
    path_data_folder = '../../data'
    dst = path_data_folder+'/'+case_name

    if os.path.exists(dst) == False:
        os.system('mkdir '+dst)

    if os.path.exists('./temp_img_0') == True:
        os.system('mv ./temp_img_0 '+dst+'/temp_img_0')
        print('MOVED temp_img_0')

    if os.path.exists('./temp_img_1') == True:
        os.system('mv ./temp_img_1 '+dst+'/temp_img_1')
        print('MOVED temp_img_1')

    if os.path.exists('./video') == True:
        os.system('mv ./video '+dst+'/video')
        print('MOVED video')

    if os.path.exists('./displacementPerFrame') == True:
        os.system('mv ./displacementPerFrame '+dst+'/displacementPerFrame')
        print('MOVED displacementPerFrame')

    if os.path.exists('./graph') == True:
        os.system('mv ./graph '+dst+'/graph')
        print('MOVED graph')

    if os.path.exists('./after_first_filter') == True:
        os.system('mv ./after_first_filter '+dst+'/after_first_filter')
        print('MOVED after_first_filter')

    if os.path.exists('./feature_point_0') == True:
        os.system('mv ./feature_point_0 '+dst+'/feature_point_0')
        print('MOVED feature_point_0')

    if os.path.exists('./feature_point_1') == True:
        os.system('mv ./feature_point_1 '+dst+'/feature_point_1')
        print('MOVED feature_point_1')

    if os.path.exists('./excel_cam_0') == True:
        os.system('mv ./excel_cam_0 '+dst+'/excel_cam_0')
        print('MOVED excel_cam_0')

    if os.path.exists('./excel_cam_1') == True:
        os.system('mv ./excel_cam_1 '+dst+'/excel_cam_1')
        print('MOVED excel_cam_1')

#===========================================
