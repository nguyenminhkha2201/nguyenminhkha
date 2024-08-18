# -*- coding: utf-8 -*-
"""
Created on Sat Aug 17 16:07:48 2024

@author: NGUYENMINHKHA 
"""
#Bài tập tính tiền taxi
distance = float (input("Nhập số km quãng đường đi được: "))


    #1km đầu tiên
if distance ==1:
    tongtien= 20
    print("Tổng tiền: ",tongtien )
    #3km đầu tiên
elif distance <=3 :
    tongtien= 13*distance 
    print("Tổng tiền: ",tongtien )
        
    #từ km thứ 4 đến km thứ 8
elif distance <=8:
    tongtien= 3*13 + (distance -3)*12
    print("Tổng tiền: ",tongtien )
        
    #Giá còn lại
else: 
    tongtien=3*13 + 5*12 + (distance - 8)*10 
    
    #Áp dụng giảm giá
if tongtien >= 100:
    tongtien=tongtien*0.92
        
    print("Tổng tiền taxi cần trả là: ", tongtien)
else: 
    print("Không xác định")
   