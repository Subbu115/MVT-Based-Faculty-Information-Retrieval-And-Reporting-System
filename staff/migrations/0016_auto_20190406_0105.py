# Generated by Django 2.1.5 on 2019-04-05 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0015_auto_20190406_0104'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personaldetails',
            name='aadharnumber',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='personaldetails',
            name='alternatemobile',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='personaldetails',
            name='mobile',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='personaldetails',
            name='pancardnumber',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='personaldetails',
            name='pincode',
            field=models.IntegerField(),
        ),
    ]