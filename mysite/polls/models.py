from django.db import models

class Image(models.Model):
    imgName = models.CharField(max_length=200)
    img = models.ImageField(null = True)
    imgDate = models.DateField(auto_now_add=True)
    def __str__(self):
        return self.imgName
    def saveImg(self,name, imgs):
        self.imgName = name
        self.img = imgs

class Document(models.Model):
    SCMT = models.CharField(max_length = 12)
    NS = models.CharField(max_length = 8)
    

