#SOIT108_Advance_011
a=int(input())
h=a//60//60 #hour
m=a//60%60 #minute
s=a%60
print(f'{h:02}:{m:02}:{s:02}',end='') #we need 00 to return ans