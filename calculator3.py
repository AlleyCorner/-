#! /usr/bin/env python3

import sys
from multiprocessing import Process,Queue,Lock

que1 = Queue()
que2 = Queue()

args = sys.argv[1:]
index = args.index('-c')
configfile = args[index+1]
index = args.index('-d')
userdatafile = args[index+1]
index = args.index('-o')
outputfile = args[index+1]
def userdata():
    lists = []
    with open(userdatafile,'r') as files:
        for line in files.readlines():
            item = line.split(',')
            lists.append(item[0].strip())
            lists.append(item[1].strip())
    que1.put(lists)

def get_social(config):
    count = 0.00
    for key,value in config.items():

        if str(key) == 'JiShuL':
             continue
        elif str(key) == 'JiShuH':
             continue
        else:
             count += float(value)
    return count

def cal(value,config,count):

        if(float(value) <= float(config['JiShuL'])):
            social = float(config['JiShuL'])*count
        elif(float(value) >= float(config['JiShuH'])):
            social = float(config['JiShuH'])*count
        else:
            social = float(value)*count
        return social

def get_tax(pay,social):
     try:
         c = pay
         a = c-social-3500
     except:
         print("Parameter Error")
     if(a <= 0):
         b = 0.00
     elif(a <= 1500 and a>=0):
         b = a*0.03
     elif(a>1500 and a<=4500):
         b = a*0.1-105
     elif(a>4500 and a<=9000):
         b = a*0.2-555
     elif(a>9000 and a<=35000):
         b = a*0.25-1005
     elif(a>35000 and a<=55000):
         b = a*0.3-2755
     elif(a>55000 and a<=80000):
         b = a*0.35-5505
     elif(a>80000):
         b = a*0.45-13505
     else:
         print("Error!")
         b = 0.00
     return b,c-b-social


def calculator():
    newdata = []
    config = {}
    data = que1.get()
    with open(configfile,'r') as files:
        for line in files.readlines():
            if not line:
                continue
            item = line.split('=')
            key = item[0].strip()
            value = item[1].strip()
            config[key] = value
    count = get_social(config)
    for i in data[::2]:
        ID = int(i)
        pay = int(data[data.index(i)+1])
        social = cal(pay,config,count)
        tax,salary = get_tax(pay,social)
        strnewdata =  str(ID)+','+str(pay)+','+str(format(social,'.2f'))+','+str(format(tax,'.2f'))+','+str(format(salary,'.2f'))
        newdata.append(strnewdata)
    que2.put(newdata)

def writefile():
    data = que2.get()
    with open(outputfile,'a') as files:
        for i in data:
            files.write(i)
            files.write('\n')


'''
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
'''
 
def main():
    lock = Lock()
    Process(target = userdata).start()
    Process(target = calculator).start()
    Process(target = writefile).start()

if __name__ == '__main__':
    main()
