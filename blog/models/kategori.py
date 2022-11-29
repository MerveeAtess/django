#yazılar-yorum-kategori 
from django.db import models 
#model oluşturma 
from autoslug import AutoSlugField


class KategoriModel(models.Model): 
    name=models.CharField(max_length=30,blank=False,null=False) 
    #kat. isimleri boş bırakılmasın 
    slug=AutoSlugField(populate_from="name",unique=True) #alanları oluşturma-otomatik isimden türeme olsun paket yükledik 
#pipenv install django-autoslug 
    class Meta: 
        db_table='kategori' 
    #sqlitedaki adını seçiyoruz
        verbose_name_plural="Kategoriler"
        #sol tarafta kategoriler yazsın
        verbose_name="kategori"
        #select kısmında kategori yazılacak


    def __str__(self):
        return self.name 
    #kategorilere ismi bassın

