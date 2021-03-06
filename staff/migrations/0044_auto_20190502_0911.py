# Generated by Django 2.1.5 on 2019-05-02 03:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('staff', '0043_auto_20190502_0854'),
    ]

    operations = [
        migrations.CreateModel(
            name='Phds_Degree',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('degreename', models.CharField(max_length=400)),
                ('collegename', models.CharField(max_length=400)),
                ('University', models.CharField(max_length=400)),
                ('specification', models.CharField(max_length=500)),
                ('yearofpassing', models.CharField(max_length=500)),
                ('result', models.CharField(max_length=600)),
                ('percentage', models.CharField(max_length=100)),
                ('emailid', models.EmailField(max_length=254)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='phd_degree',
            name='user',
        ),
        migrations.DeleteModel(
            name='Phd_Degree',
        ),
    ]
