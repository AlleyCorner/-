#! /usr/bin/env python3

import sys
args = sys.argv[1:]
index = args.index('-c')
configfile = args[index+1]
index = args.index('-d')
userdatafile = args[index+1]
index = args.index('-o')
outputfile = args[index+1]

class Config(object):
    def __init__(self,configfile):
        self._config = {}
        with open(configfile,'r') as files:
            for line in files.readlines():
                if not line:
                    continue
                item = line.split('=')
                key = item[0].strip()
                value = item[1].strip()
                self._config[key] = value
    def get_config(self,text):
        return self._config[text]
    def get_social(self):
        count = 0.00
        for key,value in self._config.items():
            if str(key) == 'JiShuL':
                continue
            elif str(key) == 'JiShuH':
                continue
            else:
                count += float(value)
        return count
class UserData(object):
    def __init__(self,userdatafile):
        self.userdata = {}
        with open(userdatafile,'r') as files:
            for line in files.readlines():
                item = line.split(',')
                key = item[0].strip()
                value = item[1].strip()
                self.userdata[key] = value
    def cal(self,value):
         config = Config(configfile)
         if(float(value) <= float(config.get_config('JiShuL'))):
             social = float(config.get_config('JiShuL'))*config.get_social()
         elif(float(value) >= float(config.get_config('JiShuH'))):
             social = float(config.get_config('JiShuH'))*config.get_social()
         else:
             social = float(value)*float(config.get_social())
         return social
    def calculator(self,pay,social):
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
    def dumptofile(self,outputfile):
        with open(outputfile,'a') as files:
            for key,value in self.userdata.items():
                lists=[]
                ID = int(key)
                pay = int(value)
                social = self.cal(value)
                tax,salary = self.calculator(pay,social)
                files.write(str(ID)+','+str(pay)+','+str(format(social,'.2f'))+','+str(format(tax,'.2f'))+','+str(format(salary,'.2f')))
                files.write("\n")
try:
    textfile = UserData(userdatafile)
    textfile.dumptofile(outputfile)
except:
    print('Error')
