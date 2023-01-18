# Generated by Django 4.1.3 on 2023-01-18 12:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_auto_20230118_1310'),
    ]

    operations = [
        migrations.AlterField(
            model_name='allotment',
            name='c_id',
            field=models.ForeignKey(db_column='c_id', on_delete=django.db.models.deletion.CASCADE, to='account.contractor'),
        ),
        migrations.AlterField(
            model_name='allotment',
            name='p_id',
            field=models.ForeignKey(db_column='p_id', on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='account.pothole'),
        ),
    ]
