# Generated by Django 3.2.16 on 2022-10-20 15:51

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('movieapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='img',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='gallery'),
            preserve_default=False,
        ),
    ]
