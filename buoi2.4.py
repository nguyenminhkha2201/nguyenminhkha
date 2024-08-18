# -*- coding: utf-8 -*-
"""
Created on Sat Aug 17 14:55:04 2024

@author: NGUYENMINHKHA 
"""

a=float(input("Nhập cạnh a: "))
b=float(input("Nhập cạnh b: "))
c=float(input("Nhập cạnh c: "))
if a+b>c and b+c>a and a+c>b:
    #tam giác đều
   if  a == b == c :
        print("a,b,c là 3 cạnh của tam giác và đây là tam giác đều")
    #tam giác cân
   elif  a == b or b == c or a == c :
        print("a,b,c là 3 cạnh tam giác và là tam giác cân")
    #tam giác vuông
   elif  a**2 + b**2==c**2 or a**2 + c**2==b**2 or b**2+c**2==a**2 :
        print ("a,b,c là 3 cạnh tam giác và là tam giác vuông")
   else:
        print("a,b,c là 3 cạnh của tam giác ")
else: 
        print("a,b,c không là 3 cạnh của tam giác ")