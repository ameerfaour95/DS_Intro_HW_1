def my_func(x1,x2,x3):
    numerator=float((x1+x2+x3)*(x2+x3)*x3)
    denominator=float(x1+x2+x3)
    if denominator==0:
        return 'Not a number-denominator equals zero'
    elif type(x1) is not float or type(x2) is not float or type(x3) is not float:
        return 'Error: parameters should be double'
    else:
        return numerator/denominator


def convert(hours, minutes=0):
    if hours<0 or minutes<0:
        return 'Input error!'
    h=hours*60*60
    min=minutes*60
    return h+min

