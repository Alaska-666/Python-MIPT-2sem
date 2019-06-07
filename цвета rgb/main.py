import math


def is16(s):
    try:
        int(s, 16)
        return True
    except ValueError:
        return False


def f(s):
    l = len(s)
    integ = []
    i = 0
    while i < l:
        s_int = ''
        a = s[i]
        while '0' <= a <= '9':
            s_int += a
            i += 1
            if i < l:
                a = s[i]
            else:
                break
        i += 1
        if s_int != '':
            integ.append(int(s_int))
    return integ

s = input()
out = 'ERROR'
s = s.replace(' ', '')
if s.find('#') != -1:
    s = s[s.find('#'):]
    if is16(s[1:3]):
        out = str(int(s[1:3], 16)) + ' '
    else:
        out = 'ERROR'
    if is16(s[3:5]) and out != 'ERROR':
        out = out + str(int(s[3:5], 16)) + ' '
    else:
        out = 'ERROR'
    if is16(s[5:]) and out != 'ERROR':
        out = out + str(int(s[5:], 16))
    else:
        out = 'ERROR'
elif s.find('-') == -1:
    ch = f(s)
    if len(ch) == 3:
        if ch[0] < 256 and ch[1] < 256 and ch[2] < 256 and s.find('%') == -1:
            s = s.replace(str(ch[0]), '')
            s = s.replace(str(ch[1]), '')
            s = s.replace(str(ch[2]), '')
            if s == 'rgb(,,)' or str == ',,':
                out = str(ch[0]) + ' ' + str(ch[1]) + ' ' + str(ch[2])
            if s == 'rbg(,,)':
                out = str(ch[0]) + ' ' + str(ch[2]) + ' ' + str(ch[1])
            if s == 'grb(,,)':
                out = str(ch[1]) + ' ' + str(ch[0]) + ' ' + str(ch[2])
            if s == 'gbr(,,)':
                out = str(ch[2]) + ' ' + str(ch[0]) + ' ' + str(ch[1])
            if s == 'brg(,,)':
                out = str(ch[1]) + ' ' + str(ch[2]) + ' ' + str(ch[0])
            if s == 'bgr(,,)':
                out = str(ch[2]) + ' ' + str(ch[1]) + ' ' + str(ch[0])
        if ch[0] < 101 and ch[1] < 101 and ch[2] < 101:
            if s == 'rgb(' + str(ch[0]) + '%,' + str(ch[1]) + \
                    '%,' + str(ch[2]) + '%)':
                out = str(math.floor(int(ch[0])*255/100)) + ' '
                out += str(math.floor(int(ch[1])*255/100)) + ' '
                out += str(math.floor(int(ch[2])*255/100))
            if s == 'rbg(' + str(ch[0]) + '%,' + str(ch[1]) + \
                    '%,' + str(ch[2]) + '%)':
                out = str(math.floor(int(ch[0])*255/100)) + ' '
                out += str(math.floor(int(ch[2])*255/100))
                out += ' ' + str(math.floor(int(ch[1])*255/100))
            if s == 'grb(' + str(ch[0]) + '%,' + str(ch[1]) + \
                    '%,' + str(ch[2]) + '%)':
                out = str(math.floor(int(ch[1])*255/100)) + ' '
                out += str(math.floor(int(ch[0])*255/100)) + ' '
                out += str(math.floor(int(ch[2])*255/100))
            if s == 'gbr(' + str(ch[0]) + '%,' + str(ch[1]) + \
                    '%,' + str(ch[2]) + '%)':
                out = str(math.floor(int(ch[2])*255/100)) + ' '
                out += str(math.floor(int(ch[0])*255/100)) + ' '
                out += str(math.floor(int(ch[1])*255/100))
            if s == 'brg(' + str(ch[0]) + '%,' + str(ch[1]) + \
                    '%,' + str(ch[2]) + '%)':
                out = str(math.floor(int(ch[1])*255/100)) + ' '
                out += str(math.floor(int(ch[2])*255/100)) + ' '
                out += str(math.floor(int(ch[0])*255/100))
            if s == 'bgr(' + str(ch[0]) + '%,' + str(ch[1]) + \
                    '%,' + str(ch[2]) + '%)':
                out = str(math.floor(int(ch[2])*255/100)) + ' '
                out += str(math.floor(int(ch[1])*255/100)) + ' '
                out += str(math.floor(int(ch[0])*255/100))
print(out)
