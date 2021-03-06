# Generated by Django 2.1 on 2020-09-17 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portafolio', '0002_sobremi_nombre'),
    ]

    operations = [
        migrations.AddField(
            model_name='sobremi',
            name='foto',
            field=models.URLField(default=1, verbose_name='Foto de mi persona'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='sobremi',
            name='correo',
            field=models.EmailField(max_length=254, verbose_name='correo de contacto'),
        ),
        migrations.AlterField(
            model_name='sobremi',
            name='descripcion',
            field=models.TextField(verbose_name='Breve descripcion de mi persona'),
        ),
        migrations.AlterField(
            model_name='sobremi',
            name='telefono',
            field=models.CharField(max_length=8, verbose_name='telefono de contacto'),
        ),
    ]
