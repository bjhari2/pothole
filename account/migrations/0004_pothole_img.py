# Generated by Django 4.1.3 on 2023-01-08 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_pothole'),
    ]

    operations = [
        migrations.AddField(
            model_name='pothole',
            name='img',
            field=models.ImageField(default='NULL', upload_to=''),
        ),
    ]