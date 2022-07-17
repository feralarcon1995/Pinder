# Generated by Django 4.0.5 on 2022-07-16 17:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pinderApp', '0019_rename_usuario_post_user_rename_usuario_usuario_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='profile_pics')),
                ('dni', models.PositiveIntegerField(null=True)),
                ('sexo', models.CharField(choices=[('1', 'Masculino'), ('2', 'Femenino'), ('3', 'Prefiero no decirlo')], max_length=30)),
                ('edad', models.PositiveIntegerField(null=True)),
                ('telefono', models.PositiveIntegerField(null=True)),
                ('localidad', models.CharField(max_length=50)),
                ('provincia', models.CharField(max_length=30)),
                ('ocupacion', models.CharField(max_length=50)),
                ('carga_horaria', models.PositiveIntegerField(null=True)),
                ('dias_homeoffice', models.PositiveIntegerField(null=True)),
                ('cantidad_hijos', models.PositiveIntegerField(null=True)),
                ('cantidad_mascotas', models.PositiveIntegerField(null=True)),
                ('especie_mascota', models.CharField(max_length=50)),
                ('espacio_abierto', models.CharField(choices=[('1', 'Patio o Parque'), ('2', 'Terraza o Balcon'), ('3', 'No poseo')], max_length=40)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='Usuario',
        ),
    ]