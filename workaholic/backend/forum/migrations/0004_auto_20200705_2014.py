# Generated by Django 3.0.6 on 2020-07-05 12:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0017_delete_notification'),
        ('forum', '0003_auto_20200705_1951'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='receiver',
        ),
        migrations.RemoveField(
            model_name='post',
            name='sender',
        ),
        migrations.AddField(
            model_name='post',
            name='posted_by',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='msg_sender', to='accounts.Project_Member'),
        ),
        migrations.AddField(
            model_name='post',
            name='thread',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='thread_post', to='accounts.Project'),
        ),
        migrations.AlterField(
            model_name='post',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='project_post', to='accounts.Project'),
        ),
        migrations.CreateModel(
            name='Thread',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60, null=True)),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='thread_creater', to='accounts.Project')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='project_thread', to='accounts.Project')),
            ],
        ),
    ]