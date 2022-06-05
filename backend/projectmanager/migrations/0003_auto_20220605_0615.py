# Generated by Django 3.2.13 on 2022-06-05 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projectmanager', '0002_project_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='images',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='project',
            name='tools',
            field=models.TextField(blank=True, null=True),
        ),
    ]
