# -*- coding: utf-8 -*-
"""
Created on Sat Aug 17 14:52:49 2024

@author: NGUYENMINHKHA
"""

a= float(input("nhập số thực a: "))
b= float(input("nhập số thực b: "))
c= float(input("nhập số thực c: "))
delta=float(b**2-4*a*c)
if delta == 0:
    print("Phương trình có nghiệm kép", - b/(2*a))
elif delta > 0 :
    print("Phương trình có 2 nghiệm phân biệt là:  ",(- b+delta**0.5)/(2*a),"và ", (- b - delta**0.5)/(2*a) )
else:
    print("Phương trình vô nghiệm")