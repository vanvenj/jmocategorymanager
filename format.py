# -*- coding: utf-8 -*-
import re
import sys
from collections import Counter

def main():
    sourcefile = sys.argv[1]
    newcode = sys.argv[2].upper()
    newpath = sys.argv[3].upper()

    # open source file
    with open(sourcefile, 'r') as f:
        data = repr(f.read())

    # define the keywords pattern of category member who has names
    cate = re.compile(r'(?<=\sCATEGORY\s/).+?(?=\\n)',  flags=re.I)
    sdte = re.compile(r'(?<=\sSDTEXT\s/).+?(?=\\n)',  flags=re.I)
    text = re.compile(r'(?<=\sTEXT\s/).+?(?=\\n)',  flags=re.I)
    scom = re.compile(r'(?<=\sSCOMPONENT\s/).+?(?=\\n)', flags=re.I)
    ptse = re.compile(r'(?<=\sPTSET\s/).+?(?=\\n)', flags=re.I)
    gmse = re.compile(r'(?<=\sGMSET\s/).+?(?=\\n)', flags=re.I)
    old = re.compile(r'(?<=OLD\s/).+?(?=\\n)', flags=re.I)

    # solve category
    if Counter(cate.findall(data)).__len__() != 1:
        print('Too many CATEGORY names!')
        return
    data = cate.sub(newcode, data)

    # solve sdte 
    if Counter(sdte.findall(data)).__len__() > 1:        
        print('Too many SDTEXT names!')
        return
    data = sdte.sub(newcode+'-SDTE', data)

    # solve text 
    try:
        data = text.sub(lambda m:newcode + '-' + re.findall(r'PA\d+|PTSE|GMSE|ISS', m.group(0), flags=re.I)[0], data)
    except Exception as e:
        print('Something wrong in TEXT')
        print(e)
        return

    # solve scomponent
    data = scom.sub(lambda m: newcode + m.group(0)[-2:], data)

    # solve PTSE
    if Counter(ptse.findall(data)).__len__() != 1:
        print('PTSE error!')
        return
    data = ptse.sub(newcode+'-P', data)

    # solve GMSE
    if Counter(gmse.findall(data)).__len__() != 1:
        print('GMSE error!')
        return
    data = gmse.sub(newcode+'-G', data)

    # delete the lines which only do locate and lock
    data = re.sub(r'OLD\s[/A-Za-z0-9-.\s]+\\nLOCK', '', data, flags=re.I)

    # solve OLD line
    # this could be some error
    # i think old is only for scom now 
    data = old.sub(lambda m: newcode + m.group(0)[-2:], data)

    # delete lock status
    data = re.sub(r'LOCK', '', data)

    # delete two end
    data = re.sub(r'END\\nEND', 'END', data)
    
    # delete INPUT END line
    data = re.sub(r'INPUT\sEND.+(?=\\n)', '', data)

    # save the file
    # with open('E:\\' + newcode+'.txt', 'w') as f:
    with open(newpath, 'w') as f:
        f.write(eval(data))
    print('Convert Success !')

if __name__ == '__main__':
    if sys.argv.__len__() != 4:
        print('\n  Usage:\n\tpython format.py source.txt NEWCODE NEWPATH\n\n')
    else:
        main()
