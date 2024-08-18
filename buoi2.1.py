# -*- coding: utf-8 -*-
"""
Created on Sat Aug 17 13:50:53 2024

@author: NGUYEMINHKHA 
"""


GPA= float(input("Nhập điểm trung bình (GPA):"))
if GPA < 3.5:
    print("Học lực kém")
elif GPA >=3.5 and  GPA < 5.0:
    print("Học lực yếu")
elif GPA >=5.0 and GPA <7.0:
    print("Học lực trung bình")
elif GPA >= 7.0 and  GPA < 8.0:
    print("Học lực khá")
elif GPA >= 8.0 and GPA < 9.0:
    print("học lực giỏi")
elif GPA >= 9.0 and GPA <= 10:
    print( "học lực xuất sắc")