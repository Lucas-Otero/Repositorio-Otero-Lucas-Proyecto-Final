# Generated by Django 4.1.7 on 2023-04-02 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prueba', '0002_usuario'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usuario',
            old_name='contrasena',
            new_name='password',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='correo',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='usuario',
        ),
        migrations.AddField(
            model_name='usuario',
            name='email',
            field=models.EmailField(default=1, max_length=254, unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='usuario',
            name='username',
            field=models.CharField(default=1, max_length=50, unique=True),
            preserve_default=False,
        ),
    ]
