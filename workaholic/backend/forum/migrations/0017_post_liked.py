# Generated by Django 3.0.7 on 2020-07-15 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0016_auto_20200715_1844'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='liked',
            field=models.BooleanField(default=False),
        ),
    ]
