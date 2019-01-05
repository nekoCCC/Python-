#-*-coding:utf-8-*-

a=0o101
print("a="+str(a))

b=64
print("b="+str(b))

c=-237
print("c="+str(c))

d=0x80
print("d="+str(d))

e=-0x92
print("e="+str(e))

foo=42
bar=foo<42

print(bar)        #false
print(bar+10)	  #10
print('%s'%bar)	  #false
print('%d'%bar)   #0

#无_nozero_():True
print(0.0)
print(-777)
print(-5.555567119)
print(96e3*1.0)
print(-1.609E-19)

#复数
print(complex(2,4))
print(1.23e-045+6.7e+089j)

#十进制浮点型

from decimal import *
#引入decimal模块，在通过Decimal类初始化一个Decimal对象
print ("十进制浮点型......")
dec=Decimal('.1')
print(dec)
print(Decimal(.1))
print(dec+Decimal(.1))

#转换工厂

print("转换工厂：！")
print(int(4.2222222))
print(float(4))
print(complex(4))

#进制转换

print("进制转换")
print(hex(255))
print(oct(255))
print(oct(0x111))

print("进制转换")
print(chr(76))
print(ord('L'))