# Generated by Django 4.2.4 on 2023-09-13 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storeapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(null=True, upload_to='media/'),
        ),
    ]
