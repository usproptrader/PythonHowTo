
str1 ='abcdef'
str2 = "123456789"
int4=[1,2,3,4,5]
n1 = 3
n2 = 4

str3 = str1,str2                # makes a tuple  (a,b)
str4,str5 = str3                # unpacks a tuple
str6 =[str1,str2,str3]          # amkes a list
str6 += [str4,str5]             # adds  to a list

print(str6)
str7 = str1[0]                  # 'a'
num1 = str1.index("d")          # is = 3
str7 = str1[0]                  # 'a'
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
strI = "\n".join(((i+"="+str(eval(i))) for i in strH))
# makes str1='abcdef' ...join with (cr)
print(strI)

s5 =slice(4,1,-1)               # equiv to  1:4:-1
s6= str2[s5]                    #543
ss=(lambda x,y :x+y)            #<function <lambda> at 0x039E5540>
str3=ss(str1,str2)              #abcdef123456789
tt=(lambda x,y : x*y)
print ('ss='+str(ss(n1,n2)))    #7
print ('tt='+str(tt(n1,n2)))    #12

del int4 [2]                    #[1,2,4,5]
print ("int4="+str(int4))
str6=''
for i in reversed(str2): str6+= i
print ('str6= '+str6)           #'987654321'
int7=[]
for i in reversed(int4): int7 += [i]
print( "int7="+str(int7))       #[5,4,2,1]
strJ="".join(str (i) for i in reversed (int4)) #5421
print ("strJ= " + strJ)

t='hold'