from django.db import models
from django.contrib.auth.models import User
from blog.models import YaziModel

class YorumModel(models.Model):
    yazan= models.ForeignKey(User, on_delete=models.CASCADE,related_name="yorum")
    yazi=models.ForeignKey(YaziModel,on_delete=models.CASCADE,related_name="yorumlar")
    #yazının yorumlarına ulaşmak için ters ilişki kurduk
    yorum=models.TextField()
    olusumtarih=models.DateTimeField(auto_now_add=True)
    guncellemetarihi=models.DateTimeField(auto_now=True)

class Meta:
    db_table="yorum"
    verbose_name="Yorum"
    verbose_name_plural="Yorumlar"

def __str__(self):
    return self.yazan.username