# Generated by Django 5.1 on 2024-08-30 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_post_options_post_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(default='blog/feature-img5.jpg', upload_to='blog/'),
        ),
    ]
