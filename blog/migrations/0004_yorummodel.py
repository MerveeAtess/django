# Generated by Django 4.1.1 on 2022-12-03 17:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0003_yazimodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='YorumModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('olusumtarih', models.DateTimeField(auto_now_add=True)),
                ('guncellemetarihi', models.DateTimeField(auto_now=True)),
                ('yazan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='yorum', to=settings.AUTH_USER_MODEL)),
                ('yazi', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='yorumlar', to='blog.yazimodel')),
            ],
        ),
    ]
