from django.contrib import admin
from polls.models import Image
# Register your models here.
#class ImgAdmin(admin.ModelAdmin):
    #list_display = ['imgUrl','img']
admin.site.register(Image)