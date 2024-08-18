# -*- coding: utf-8 -*-
"""
Created on Sat Aug 17 13:22:10 2024

@author: NGUYENMINHKHA
"""

distance = float(input("nhập độ dài đoạn đường đến trường(m):"))
if distance< 300:
    print("đường đến trường quá gần. Thôi đi bộ")
elif distance >= 1200 :
    print("đường đến trường không xa. thôi đi xe máy")
elif distance >= 300 and distance <= 700:
    print("đường đến trường không xa. Thôi đi xe đạp.")
else:
    print("Không xác định")
 
    