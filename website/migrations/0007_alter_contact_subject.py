# Generated by Django 5.1 on 2024-09-07 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0006_alter_contact_subject'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='subject',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
