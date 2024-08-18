# -*- coding: utf-8 -*-
"""
Created on Sat Aug 17 15:15:24 2024

@author: NGUYENMINHKHA 
"""
#Bài tập kéo búa bao 
import random 
print ("Chào mừng bạn đến với trò chơi kéo - búa - bao!")
nguoi_chon = input("Nhập lựa chọn của bạn: ")
if nguoi_chon == "kéo" or nguoi_chon == "búa" or nguoi_chon == "bao":
    
    may_chon=random.choice(["kéo","búa","bao"])
    print("Máy chọn: ",may_chon)

    if nguoi_chon == may_chon:
        print("hòa")
    elif (nguoi_chon == "kéo" and may_chon == "bao") or (nguoi_chon == "búa" and may_chon == "kéo") or (nguoi_chon == "bao" and may_chon == "búa"):
        print("Bạn thắng")
    else:
        print ("Bạn thua")
else: 
    print ("Lỗi. Mời nhập lại")