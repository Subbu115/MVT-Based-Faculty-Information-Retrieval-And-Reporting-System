# Generated by Django 2.1.5 on 2019-05-02 04:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('staff', '0045_auto_20190502_0916'),
    ]

    operations = [
        migrations.CreateModel(
            name='Publications_Details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titleofpublication', models.CharField(max_length=600)),
                ('authorname', models.CharField(max_length=600)),
                ('year', models.DateField()),
                ('titleofpaper', models.CharField(max_length=600)),
                ('volume', models.CharField(max_length=600)),
                ('pagenumbers', models.CharField(max_length=600)),
                ('impact', models.CharField(max_length=600)),
                ('reviewer', models.CharField(max_length=600)),
                ('journalname', models.CharField(max_length=600)),
                ('emailid', models.EmailField(max_length=254)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='publication_details',
            name='user',
        ),
        migrations.DeleteModel(
            name='Publication_Details',
        ),
    ]
