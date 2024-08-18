# -*- coding: utf-8 -*-
"""
Created on Sat Aug 17 16:48:28 2024

@author: NGUYENMINHKHA 
"""

ngay= int(input("nhập ngày: "))
thang= int(input("nhập tháng: "))
nam= int(input("nhập năm: "))

if nam % 400 == 0 or (nam % 4 == 0 and nam % 100 != 0):
    nam_nhuan= True 
else:
    nam_nhuan= False
if thang == 2 :
    if nam_nhuan:
        so_ngay_trong_thang = 29
    else:
        so_ngay_trong_thang = 28
elif thang in [4, 6, 9, 11]:
    so_ngay_trong_thang = 30
else:
    so_ngay_trong_thang = 31

# Kiểm tra ngày và tháng hợp lệ
if 1 <= thang <= 12:
    if 1 <= ngay <= so_ngay_trong_thang:
        if nam_nhuan:
            print(f"Năm {nam} là năm nhuận.")
        else:
            print(f"Năm {nam} không phải là năm nhuận.")
    else:
        print(f"{ngay}/{thang}/{nam} không phải là ngày hợp lệ.")
else:
    print(f"{thang}/{nam} không phải là tháng hợp lệ.")
