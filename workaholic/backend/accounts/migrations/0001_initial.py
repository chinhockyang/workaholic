# Generated by Django 3.0.7 on 2020-07-10 11:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Project_Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('calendar_month', models.DateTimeField()),
                ('cal_last_modified', models.DateTimeField(null=True)),
                ('board_last_modified', models.DateTimeField(null=True)),
                ('last_modified', models.DateTimeField(null=True)),
                ('board_last_modified_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='board_last_modified', to='accounts.Project_Member')),
                ('cal_last_modified_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cal_last_modified', to='accounts.Project_Member')),
                ('last_modified_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='project_last_modified', to='accounts.Project_Member')),
                ('project_admin', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
                ('project_members', models.ManyToManyField(to='accounts.Project_Member')),
            ],
        ),
    ]
