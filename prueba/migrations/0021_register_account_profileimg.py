# Generated by Django 4.1.7 on 2023-04-22 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prueba', '0020_delete_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='register_account',
            name='profileimg',
            field=models.ImageField(default='', upload_to='profile_images/'),
        ),
    ]
