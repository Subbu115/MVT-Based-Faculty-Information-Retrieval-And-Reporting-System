# Generated by Django 2.1.5 on 2019-06-05 12:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0057_auto_20190506_2029'),
    ]

    operations = [
        migrations.AlterField(
            model_name='facultydetails',
            name='department',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='departments.Department'),
        ),
    ]
