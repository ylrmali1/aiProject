# Generated by Django 4.1.7 on 2023-03-21 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='project_image',
            field=models.ImageField(upload_to='project-images/'),
        ),
    ]
