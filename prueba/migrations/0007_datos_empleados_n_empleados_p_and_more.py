# Generated by Django 4.1.7 on 2023-04-09 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prueba', '0006_recipe'),
    ]

    operations = [
        migrations.CreateModel(
            name='Datos_Empleados',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('puesto', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='N_Empleados_P',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('sector', models.CharField(max_length=50)),
                ('correo', models.EmailField(max_length=100)),
            ],
        ),
        migrations.RenameModel(
            old_name='Recipe',
            new_name='N_Emp_Total',
        ),
        migrations.DeleteModel(
            name='Login',
        ),
        migrations.DeleteModel(
            name='Register',
        ),
    ]
