# Generated by Django 4.0.5 on 2022-07-12 21:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pinderApp', '0005_alter_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(null=True, upload_to='posteos'),
        ),
    ]