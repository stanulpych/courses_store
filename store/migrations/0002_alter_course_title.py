# Generated by Django 4.2.9 on 2024-02-02 02:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='title',
            field=models.CharField(max_length=55),
        ),
    ]
