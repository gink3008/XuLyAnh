from django.http import HttpResponse 
from django.shortcuts import render, redirect 
from .models import *
from django.core.files.storage import FileSystemStorage
import polls.api1 
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
        Posts = [((1,2,3,4),(1,2,3,4)),((1,2,3,4),(1,2,3,4))] 
        #api1(url)
        return redirect('profile')
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