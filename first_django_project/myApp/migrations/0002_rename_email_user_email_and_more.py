# Generated by Django 4.0 on 2021-12-17 11:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='email',
            new_name='Email',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='f_name',
            new_name='First_Name',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='l_name',
            new_name='Last_Name',
        ),
    ]
