# Generated by Django 4.0.4 on 2022-05-10 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0003_worker'),
    ]

    operations = [
        migrations.AddField(
            model_name='worker',
            name='Worker_img',
            field=models.ImageField(default=1, upload_to='pics'),
            preserve_default=False,
        ),
    ]
