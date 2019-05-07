import numpy as np
import cv2
# hàm soft từ trên xuống để lấy các hàng
def sorty(c):
    x,y,w,h = cv2.boundingRect(c)
    return y
# hàm soft vị trí trong 1 hàng
def sortx(c):
    x,y,w,h =cv2.boundingRect(c)
    return x 
# cắt các ảnh
def createImg(img,lists,num,l,list_img):
    for c in lists:
        x,y,w,h=cv2.boundingRect(c)
        if w>20 and h >20:
                #ảnh lấy đc
                new_img=img[y+l:y+h-l,x+l:x+w-l]   #bỏ khung 
                new_img=cv2.resize(new_img,(28,28),interpolation=cv2.INTER_CUBIC) #resize 28*28
                list_img.append(new_img)              #cho vào list
                cv2.imwrite(str(num)+'new.png',new_img)     #tạo các ảnh mới 
                num=num+1                          # tăng num để tạo tên
    return num
def main(url):
    #declare 
    min_h=20    # độ dài nhỏ nhất của contour
    min_w=20    #
    img=cv2.imread(url)   
    img = cv2.resize(img,(2000,1000))   #resize ảnh
    h,w,d =img.shape        # lấy các chiều của ảnh
    num=1                   # số để tạo tên ảnh
    img=img[0:h,400:w]      # cắt ảnh
    list_img=[]             # danh sách đầu ra các ảnh
    l=5                     # l để resize ảnh ,bỏ phần viền
    ct=[]                   # là mảng các contour chính xác
    # tìm tất cả contour (số lượng không chính xác)
    img0=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    res,thresh=cv2.threshold(img0,180,255,cv2.THRESH_BINARY)
    ct1,_ =cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    #tô đậm khung để detect chính xác hơn
    for c in ct1:
        x,y,w,h = cv2.boundingRect(c)
        if w > min_w and h > min_w  and cv2.contourArea(c)>400 and cv2.contourArea(c)<6000:
            cv2.drawContours(img0,[c],0,(0,255,0),1)
    # tìm các contour với số lượng chính xác (do đã tô đậm)    
    ret,thresh1 = cv2.threshold(img0,180,225,cv2.THRESH_BINARY)
    edged = cv2.Canny(thresh1, 0, 127)
    (cnts, _) = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)   
    for c in cnts:
        x,y,w,h=cv2.boundingRect(c)
        if w>min_w and h>min_h and cv2.contourArea(c)>400 and cv2.contourArea(c)<6000:
            cv2.drawContours(img, [c], 0, (0,255,0), 5)
            ct.append(c)
    #
    ct=sorted(ct,key=sorty)     #sort theo chiều dọc để lấy contour theo hàng
    n_ct=len(ct)                #số contour
    a=int((n_ct)/36 )                #lấy số người
    print(n_ct) 
    print(a)
    #
    for i in range(a):
        i=i+1
        #chia làm 3 list tương ứng với 3 hàng của mỗi người
        list1=ct[36*i-36:36*i-20]
        list1=sorted(list1,key=sortx)
        list2=ct[36*i-20:36*i-8]
        list2=sorted(list2,key=sortx)
        list3=ct[36*i-8:36*i]
        list3=sorted(list3,key=sortx)
        #
        num=createImg(img,list1,num,l,list_img)
        num=createImg(img,list2,num,l,list_img)
        num=createImg(img,list3,num,l,list_img)
    return list_img
