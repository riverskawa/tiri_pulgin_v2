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

a()