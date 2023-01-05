from django.contrib import admin
from blog.models import (KategoriModel, YaziModel,
YorumModel, IletisimModel)

admin.site.register(KategoriModel)
# Register your models here.


#yazılar customize etmek
class YaziAdmin(admin.ModelAdmin):
    search_fields=("baslik","icerik") #arama yapmak için
    list_display= (
        "baslik","olusumtarih","duzenlenmetarihi")
    
admin.site.register(YaziModel,YaziAdmin)

class YorumAdmin(admin.ModelAdmin):
    list_display=("yazan","olusumtarih","guncellemetarihi")
    search_fields=("yazan_username",)

admin.site.register(YorumModel,YorumAdmin)

class IletisimAdmin(admin.ModelAdmin):
    list_display=("email","olusumtarih")
    search_fields=("email",)

admin.site.register(IletisimModel,IletisimAdmin)