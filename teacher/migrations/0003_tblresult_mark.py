# Generated by Django 3.2.14 on 2022-12-01 06:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0002_alter_tblsubjectcombination_subjectid'),
    ]

    operations = [
        migrations.AddField(
            model_name='tblresult',
            name='mark',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
