# Generated by Django 4.1.6 on 2023-02-10 01:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('despesa', '0003_alter_ocorrencia_data_alter_ocorrencia_obs'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ocorrencia',
            name='data',
            field=models.DateTimeField(),
        ),
    ]
