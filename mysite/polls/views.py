from django.http import HttpResponse 
from django.shortcuts import render, redirect 
from .models import *
from django.core.files.storage import FileSystemStorage
from polls import api1 
from polls import api2
import cv2
import numpy
def profile(request):
    Data = {'Posts' : [((1,2,3,4),(1,2,3,4)),((1,2,3,4),(1,2,3,4,5))] }
    return render(request, 'polls/profile.html', Data)
def index(request):
    if request.method == 'POST': 
        reponse = HttpResponse()
        imgupload = request.FILES['Image'] 
        fs = FileSystemStorage()
        name = fs.save(imgupload.name,imgupload)
        url = fs.url(name)
        image = Image()
        image.saveImg(name,url)
        image.save()
        li = api1.main('.' + url)
        list_detect = api2.Detect(li)
        Post = []
        a = int(len(list_detect)/36 )
        for i in range(a):
            dong1 = list_detect[0+36*i:16+36*i-1]
            dong2 = list_detect[16+36*i:28+36*i-1]
            dong3 = list_detect[28+36*i:36+36*i-1]
            o = []
            o.append(dong1)
            o.append(dong2)
            o.append(dong3)
            Post.append(o)
        Data = {'Posts' : Post }
        return render(request, 'polls/profile.html', Data)
    return render(request, 'polls/body.html')
def index2(request):
    if request.method == 'POST': 
        imgupload = request.FILES['Image'] 
        fs = FileSystemStorage()
        name = fs.save(imgupload.name,imgupload)
        url = fs.url(name)
    return render(request, 'polls/body.html') 
def success(request): 
    return HttpResponse('successfuly uploaded')
def table(DocumentModel):
    HttpResponse.writable(DocumentModel)
        
def list(request):
    Data = {'Post' : Image.object.all().orderby("-date")}
    return render(request, 'polls/index')