from django.db import models

class IletisimModel(models.Model):
    email=models.EmailField(max_length=250)
    name_surname=models.CharField(max_length=150)
    message=models.TextField()
    olusumtarih=models.DateTimeField(auto_now_add=True)


    class Meta:
        db_table="iletisim"
        verbose_name="Iletisim"
        verbose_name_plural="iletişim"

    def __str__(self):
        return self.email