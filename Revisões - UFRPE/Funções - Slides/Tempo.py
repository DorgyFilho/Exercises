#007 - Tempo

def conv(num):
    if num < 10:
        return '000' + str(num)
    elif num < 100:
        return '00' + str(num)
    elif num < 1000:
        return '0' + str(num)
    else:
        return str(num)

