# for functions need to indent by one tab
#to move blocks of code mark first pos with mouse
# the hold alt and drag down column
# hit tab to move
import time
import os

def Func1():
    str1 ='ABCDEFGH'
    str2 = "123456789"
    int4=[1,2,3,4,5]
    n1 = 3
    n2 = 40

    str3 = str1,str2                # makes a tuple  (a,b)
    str4,str5 = str3                # unpacks a tuple
    str6 =[str1,str2,str3]          # amkes a list
    str6 += [str4,str5]             # adds  to a list
    str7 = str1[0]                  # 'a'
    num1 = str1.index("D")          # is = 3
    str8 = str2[-1]                 # "9"
    str9 = str1[1:-2]               # "bcd"
    strA = str6[2:3]                # is = to str2,str1
    strB = str1[4:1:-1]             # "edc" from e to b(exclusive) so edc
    strC=sorted(str3)               # = to str2,str1
    strD = list(reversed(strC))     # = to str1,str2
    strE = "".join(strC).upper()
    strF = "rts:".join(strE)+"rts"  # '123456789ABCDEF'
    strG = strF.split(":")          #  ['1rts',2rts',  ...
    strH = [i[::-1] for i in  strG] #  [ 'str1','str2'  ...

    s5 =slice(4,1,-1)               # equiv to  1:4:-1
    s6= str2[s5]                    #543

    sf1=(lambda x,y :x+y)            #<function <lambda> at 0x039E5540>
    str3=sf1(str1,str2)              #abcdef123456789
    sf2=(lambda x,y : x*y)
    ss3=sf1(n1,n2)                  #43
    ss4=sf2(n1,n2)                 #120

    del int4 [2]                    #[1,2,4,5]
    str6=''
    for i in reversed(str2): str6+= i #'987654321'

    int7=[]
    for i in reversed(int4): int7 += [i]  #[5,4,2,1]
    strJ="".join(str (i) for i in reversed (int4)) #5421

    print("lets print all local variables\n")
    allv= sorted(locals().keys())
    allout=""
    for varl in allv:
        allout += varl+"="+str(locals()[varl])+"\n"
    print (allout)
    time.sleep(10)
    os._exit(0)
    #if we add this code the function will run
    # when we run this file


if __name__ == "__main__":
    Func1()