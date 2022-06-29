import re
# import logging




def transferCoordinate(i2): # update:2022/05/??
    X =[]
    with open(i2, "r") as f1:
        for line in f1.readlines():
            print(line)    # testing
            # number = [int(temp)for temp in line.split() if temp.isdigit()]
            int_term_num = re.findall('\d+',line)
            print(int_term_num)
            number = re.findall("\d+\.\d+", line)    # format:string    [convect from string with dot to float]
            print(number)    # testing
            X.append([float(int_term_num[0]),float(number[0])])    # format:float  # *(-1) format:float (圖像y軸跟正常y軸倒置，所以*-1, 去反轉)

    # logging.info('type of original data: '+str(type(X))) # for test


def test(i2):
    X =[]
    with open(i2, "r") as f1:
        for line in f1.readlines():
            # number = [int(temp)for temp in line.split() if temp.isdigit()]
            number = re.findall("\d+\.\d+", line)    # format:string    [convect from string with dot to float]
            print(number)    # testing
            X.append([float(number[0]),float(number[1])])    # format:float  # *(-1) format:float (圖像y軸跟正常y軸倒置，所以*-1, 去反轉)

    print(X)
    print('len:',len(X))
    return X
    # logging.info('type of original data: '+str(type(X))) # for test

# test==========================================================
# test('./testingBox/testingData_a_threshold_normalCase_1_0_th.txt')