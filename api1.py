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
    img=cv2.imread(url)
    img = cv2.resize(img,(2000,1000))
    h,w,d =img.shape
    x=0
    num=0
    img=img[0:h,150:w]
    list_img=[]
    ###############################
    h,w,d =img.shape
    lista=[]
    ret,thresh1 = cv2.threshold(img,180,255,cv2.THRESH_BINARY)
    edged = cv2.Canny(thresh1, 0, 250)
    (cnts, _) = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    ct=[]
    for c in cnts:
        x,y,w,h=cv2.boundingRect(c)
        if w>10 and h>10 and w<80 and h<80 and cv2.contourArea(c)>80 and cv2.contourArea(c)<6000:
            cv2.drawContours(img, [c], 0, (0,255,0), 3)
            ct.append(c)
    ###############################
    ct=sorted(ct,key=sorty)
    n_ct=len(ct)
    a=(n_ct)/40
    print(n_ct)
    a=int(a)
    print(a)
    ###############################
    for i in range(a):
        i=i+1
        list1=ct[40*i-40:40*i-20]
        list1=sorted(list1,key=sortx)
        list2=ct[40*i-20:40*i-8]
        list2=sorted(list2,key=sortx)
        list3=ct[40*i-8:40*i]
        list3=sorted(list3,key=sortx)
        num=num+100
        for c in list1:
            x,y,w,h=cv2.boundingRect(c)
            if w>10 and h >10:
                new_img=img[y:y+h,x:x+w]
                new_img=cv2.resize(new_img,(28,28),interpolation=cv2.INTER_CUBIC)
                list_img.append(new_img)
                cv2.drawContours(img, [c], 0, (0,255,0), 3)
                cv2.imwrite(str(num)+'new.png',new_img)
                num=num+1
        num=num+100
        for c in list2:
            x,y,w,h=cv2.boundingRect(c)
            if w>10 and h >10:
                new_img=img[y:y+h,x:x+w]
                new_img=cv2.resize(new_img,(28,28),interpolation=cv2.INTER_CUBIC)
                list_img.append(new_img)
                cv2.drawContours(img, [c], 0, (0,255,0), 3)
                cv2.imwrite(str(num)+'new.png',new_img)
                num=num+1
        num=num+100
        for c in list3:
            x,y,w,h=cv2.boundingRect(c)
            if w>10 and h >10:
                new_img=img[y:y+h,x:x+w]
                new_img=cv2.resize(new_img,(28,28),interpolation=cv2.INTER_CUBIC)
                list_img.append(new_img)
                cv2.drawContours(img, [c], 0, (0,255,0), 3)
                cv2.imwrite(str(num)+'new.png',new_img)
                num=num+1
    cv2.imshow('sd',img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return list_img
