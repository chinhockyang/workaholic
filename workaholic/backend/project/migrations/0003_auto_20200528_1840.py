# Generated by Django 3.0.6 on 2020-05-28 10:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20200526_1459'),
        ('project', '0002_todo_added_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='added_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.Project_Member'),
        ),
    ]
