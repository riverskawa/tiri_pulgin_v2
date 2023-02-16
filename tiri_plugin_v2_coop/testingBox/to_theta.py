# input displacement

def toTheta(list_coordinate):
    # get the min. u-value
    min_u = float(9999)
    for i in range (0,len(list_coordinate)):
        if float(list_coordinate[i][0]) <= min_u:
              min_u = float(list_coordinate[i][0]) # refreshing the min_u
    rounded = round(min_u/10)*10
    min_u = rounded # to round down the min_u to tens and refresh it


def a():
    number = float(input('Enter a number :'))
    rounded = round(number/10)*10
    print('Rounded Number :', rounded)

def ins():
    lks = [1,2,3,4]
    lks.insert(0,0)
    print(lks)

def ssj():
    lk=[1,2,3,4,5,6,7,8,9,10]
    print(len(lk))
    for i in range (2,10):
        print(lk[i])

ssj()