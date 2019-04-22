import cv2
def tachanh(url):
    image = cv2.imread(url)
    gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    edged = cv2.Canny(image, 10, 250)
    (cnts, _) = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    idx = 0
    for c in cnts:
        x,y,w,h = cv2.boundingRect(c)
        if w>15 and h>15 and w<30 and h<30:
            idx+=1
            new_img=image[y:y+h,x:x+w]
            cv2.imwrite(str(idx) + 'new.png', new_img)
            cv2.imshow("im",new_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()