# Generated by Django 2.0.8 on 2018-08-28 15:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('classroom', '0014_auto_20180828_0838'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='user',
        ),
    ]
