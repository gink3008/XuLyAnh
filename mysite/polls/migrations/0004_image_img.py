# Generated by Django 2.2 on 2019-04-15 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_image_imgdate'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='img',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
