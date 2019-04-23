import numpy as np
import cv2
from django.http import HttpResponse 

##########################
def sorty(c):
    x,y,w,h = cv2.boundingRect(c)
    return y
def sortx(c):
    x,y,w,h =cv2.boundingRect(c)
    return x 
##############################
def main(url):              
        img=cv2.imread(url)
        h,w,d =img.shape
        x=0
        num=0
        ################################
        for i in range(0,w,10):
                im0=img[0:h,0:i+1]
                edged0 = cv2.Canny(im0, 0, 250)
                (cnts0, _) = cv2.findContours(edged0.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
                for c in cnts0:
                        approx = cv2.approxPolyDP(c,0.01*cv2.arcLength(c,True),True)
                if len(approx)==4:
                        img=img[0:h,i-40:w]
                        x=1
                        break
                if x==1:
                        break
                if x==1:
                        break
        #############################

        h,w,d =img.shape
        lista=[]
        edged = cv2.Canny(img, 0, 250)
        (cnts, _) = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        for c in cnts:
                x,y,w,h=cv2.boundingRect(c)
        if w>10 and h>10 and w<80 and h<80:
                cv2.drawContours(img, [c], 0, (0,255,0), 3)
        ############################
        cnts=sorted(cnts,key=sorty)
        n_cnts=len(cnts)
        a=(n_cnts)/40
        print(n_cnts)
        a=int(a)
        ##############################
        for i in range(a):
                list1=cnts[40*a-40+1:40*a-20+1]
                list1=sorted(list1,key=sortx)
                list2=cnts[40*a-20+1:40*a-8+1]
                list2=sorted(list2,key=sortx)
                list3=cnts[40*a-8+1:40*a+1]
                list3=sorted(list3,key=sortx)
                num=num+100
        for c in list1:
                x,y,w,h=cv2.boundingRect(c)
                if w>20 and h >20:
                        new_img=img[y:y+h,x:x+w]
                        cv2.drawContours(img, [c], 0, (0,255,0), 3)
                        cv2.imwrite(str(num)+'new.png',new_img)
                        num=num+1
        num=num+100
        for c in list2:
                x,y,w,h=cv2.boundingRect(c)
                if w>20 and h >20:
                        new_img=img[y:y+h,x:x+w]
                        cv2.drawContours(img, [c], 0, (0,255,0), 3)
                        cv2.imwrite(str(num)+'new.png',new_img)
                        num=num+1
        num=num+100
        for c in list3:
                x,y,w,h=cv2.boundingRect(c)
                if w>20 and h >20:
                        new_img=img[y:y+h,x:x+w]
                        cv2.drawContours(img, [c], 0, (0,255,0), 3)
                        cv2.imwrite(str(num)+'new.png',new_img)
                        num=num+1
        cv2.imshow('sd',img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        return 0