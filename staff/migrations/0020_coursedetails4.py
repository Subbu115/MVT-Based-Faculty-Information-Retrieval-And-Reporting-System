# Generated by Django 2.1.5 on 2019-04-07 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0019_delete_coursedetails'),
    ]

    operations = [
        migrations.CreateModel(
            name='coursedetails4',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=400)),
                ('code', models.CharField(max_length=500)),
                ('credit', models.IntegerField()),
                ('created', models.DateField()),
                ('department', models.CharField(max_length=600)),
                ('semester', models.IntegerField()),
                ('coursedescription', models.CharField(max_length=600)),
            ],
        ),
    ]
