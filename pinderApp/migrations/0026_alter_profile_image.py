# Generated by Django 4.0.5 on 2022-07-17 23:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pinderApp', '0025_alter_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='../media/user.png', upload_to='profile_pics'),
        ),
    ]