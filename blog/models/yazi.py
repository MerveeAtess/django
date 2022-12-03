from django.db import models
from autoslug import AutoSlugField
from blog.models import KategoriModel
from django.contrib.auth.models import User
#from ckeditor.field import RichTextField


#yazilar mdel adında class tanımlama
class YaziModel(models.Model):
    image=models.ImageField(upload_to="yazi_resimleri")
    baslik=models.CharField(max_length=50)
    icerik=models.TextField() #RichTextField
    olusumtarih=models.DateTimeField(auto_now_add=True)
    #oluşturma tarihi otomatik olacak
    duzenlenmetarihi=models.DateTimeField(auto_now_add=False)
    #duzenlenme her değiştirdiğinde bizim değiş tarih olsun diye
    slug=AutoSlugField(populate_from="baslik", unique=True)
    #urlleri göstermek için 
    kategoriler= models.ManyToManyField(KategoriModel,related_name="yazi")
    #1.parametre model ister
    #bir yazı b,rden fazla kat. eşleşebilir
    yazar=models.ForeignKey(User, related_name="yazilar", on_delete=models.CASCADE)
    #user tanımlaması olması gerek
    #btn yazılara erişmek için:related_name, yazar silindiğinde her şey silinsin:on_delete

    class Meta:
        verbose_name="Yazi"
        verbose_name_plural="Yazilar"
        db_table="yazi"


    def __str__(self):
        return self.baslik

        

