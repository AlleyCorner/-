#! /usr/bin/env python3

import sys
from multiprocessing import Process,Queue

que1 = Queue()
que2 = Queue()

args = sys.argv[1:]
idnex = args.index('-c')
configfile = args[index+1]
index = args.index('-d')
userdatafile = args[index+1]
idnex = args.index('-o')
outpufile = args[idnex+1]

class userData(object):
    def __init__
    with open(userdatafile,'r') as files:
        for line in files.readlines:
            item = line.split(',')
            lists.append(item[0].strip())
            lists.append(item[1].strip())
        que1.put(lists)

def calculator():
    newdata = []
    social = []
    data = que1.get()
    ID = data[::2]
    pay = data[1::2]
    with open(configfile,'r') as files:
        for line in files.readlines:
            item = line.split(',')
            social.append(item[0].strip())
            social.append(item[1].strip())
    social.index('JiShuL')
    social_name = social[::2]
    social_mony = social[1::2]
    
def main()
    Process(target = userdata).start()
    Process(target = calculator).start()
    Process(target = writefie).start()

if __name__ == '__main__':
    mian()
