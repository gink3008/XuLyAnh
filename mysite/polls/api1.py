import numpy as np
import cv2
###############################
def sorty(c):
    x,y,w,h = cv2.boundingRect(c)
    return y
def sortx(c):
    x,y,w,h =cv2.boundingRect(c)
    return x 
###############################
def main(url):
    #declare const
    min_h=20
    min_w=20
    img=cv2.imread(url)
    img = cv2.resize(img,(2000,1000))
    h,w,d =img.shape
    x=0
    num=0
    img=img[0:h,400:w]
    list_img=[]
    l=5
###############################
    h,w,d =img.shape
    lista=[]
    img0=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    res,thresh=cv2.threshold(img0,180,255,cv2.THRESH_BINARY)
    ct,_ =cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    #tô đậm khung 
    for c in ct:
        x,y,w,h = cv2.boundingRect(c)
        if w > min_w and h > min_w  and cv2.contourArea(c)>400 and cv2.contourArea(c)<6000:
            cv2.drawContours(img0,[c],0,(0,255,0),1)
    
    #      
    ret,thresh1 = cv2.threshold(img0,180,225,cv2.THRESH_BINARY)
    edged = cv2.Canny(thresh1, 0, 127)
    (cnts, _) = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
#     cv2.imshow("edge",edged.copy())
#     cv2.imshow("im0",img0)
#     cv2.imshow("thresh1",thresh1)
    ct=[]
    for c in cnts:
        x,y,w,h=cv2.boundingRect(c)
        if w>min_w and h>min_h and cv2.contourArea(c)>400 and cv2.contourArea(c)<6000:
            cv2.drawContours(img, [c], 0, (0,255,0), 5)
            ct.append(c)
    ###############################
    ct=sorted(ct,key=sorty)
    n_ct=len(ct)
    a=(n_ct)/36
    print(n_ct)
    a=int(a)
    print(a)
    ###############################
    for i in range(a):
        i=i+1
        list1=ct[36*i-36:36*i-20]
        list1=sorted(list1,key=sortx)
        list2=ct[36*i-20:36*i-8]
        list2=sorted(list2,key=sortx)
        list3=ct[36*i-8:36*i]
        list3=sorted(list3,key=sortx)
        num=num+100
        for c in list1:
            x,y,w,h=cv2.boundingRect(c)
            if w>min_w and h >min_h:
                new_img=img[y+l:y+h-l,x+l:x+w-l]
                new_img=cv2.resize(new_img,(28,28),interpolation=cv2.INTER_CUBIC)
                list_img.append(new_img)
                cv2.drawContours(img, [c], 0, (0,255,0), 5)
                cv2.imwrite(str(num)+'new.png',new_img)
                num=num+1
        num=num+100
        for c in list2:
            x,y,w,h=cv2.boundingRect(c)
            if w>min_w and h >min_h:
                new_img=img[y+l:y+h-l,x+l:x+w-l]
                new_img=cv2.resize(new_img,(28,28),interpolation=cv2.INTER_CUBIC)
                list_img.append(new_img)
                cv2.drawContours(img, [c], 0, (0,255,0), 5)
                cv2.imwrite(str(num)+'new.png',new_img)
                num=num+1
        num=num+100
        for c in list3:
            x,y,w,h=cv2.boundingRect(c)
            if w>min_w and h >min_h:
                new_img=img[y+l:y+h-l,x+l:x+w-l]
                new_img=cv2.resize(new_img,(28,28),interpolation=cv2.INTER_CUBIC)
                list_img.append(new_img)
                cv2.drawContours(img, [c], 0, (0,255,0), 5)
                cv2.imwrite(str(num)+'new.png',new_img)
                num=num+1
    cv2.imshow('sd',img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return list_img
