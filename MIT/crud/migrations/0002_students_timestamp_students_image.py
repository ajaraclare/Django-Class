# Generated by Django 4.2.3 on 2023-07-31 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='students',
            name='TimeStamp',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='students',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]