# Generated by Django 5.0.6 on 2024-07-31 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sumary_all', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='meetup',
            name='image',
            field=models.ImageField(default='test', upload_to='images'),
            preserve_default=False,
        ),
    ]
