from django.contrib import admin
from polls.models import Image
# Register your models here.
class ImgAdmin(admin.ModelAdmin):
    list_display = ['imgName','img','imgDate']
admin.site.register(Image,ImgAdmin)