# Generated by Django 3.0.6 on 2020-05-25 13:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='project_admin',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.Project_Admin'),
        ),
    ]