#!/usr/bin/env python3
import sys
for arg in sys.argv[1:]:
    try:
        argList=arg.split(':')
        c = int(argList[-1])
        d = c*(0.08+0.02+0.005+0.06)
        a = c-d-3500
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
    print(argList[0]+':'+format(c-d-b,".2f"))
