# Generated by Django 5.0.6 on 2024-07-01 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('custom_blog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customblogpost',
            name='saleskit_urls',
        ),
        migrations.AddField(
            model_name='customblogpost',
            name='saleskit_urls',
            field=models.URLField(max_length=1000, null=True),
        ),
    ]
