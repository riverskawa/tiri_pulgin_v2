
def run():
    with open('./testingBox/file.txt') as f:
        data = f.readlines()[0]
    print(data)

# run()

def run2():
    import re
    with open('./testingBox/0_0_th.txt') as f:
        data = f.readlines()[0]
        data_num = re.findall("\d+\.\d+", data)

        float_c = float(data_num[0])
        float_r = float(data_num[1])


run2()