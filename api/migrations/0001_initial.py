# Generated by Django 4.2.5 on 2023-10-02 12:02

import api.manager
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(choices=[(1, 'ADMIN'), (2, 'PROMOTER')], max_length=20)),
            ],
            options={
                'db_table': 'user_roles',
            },
        ),
        migrations.CreateModel(
            name='UserMaster',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('first_name', models.CharField(blank=True, max_length=255, null=True)),
                ('last_name', models.CharField(blank=True, max_length=255, null=True)),
                ('username', models.CharField(max_length=255, unique=True)),
                ('email', models.EmailField(blank=True, max_length=255, null=True, unique=True)),
                ('password', models.CharField(blank=True, max_length=100, null=True)),
                ('profile', models.FileField(blank=True, null=True, upload_to='profil_pic/')),
                ('is_staff', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('created_by', models.CharField(blank=True, max_length=100, null=True)),
                ('created_on', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('roles', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.role')),
            ],
            options={
                'db_table': 'user_master',
            },
            managers=[
                ('objects', api.manager.CustomUserManager()),
            ],
        ),
        migrations.CreateModel(
            name='SharedFiles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='')),
                ('created_on', models.DateTimeField(auto_now_add=True, null=True)),
                ('shared_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shared_files_by', to='api.usermaster')),
                ('shared_to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shared_files_to', to='api.usermaster')),
            ],
            options={
                'db_table': 'user_shareed_files',
            },
        ),
        migrations.AddIndex(
            model_name='usermaster',
            index=models.Index(fields=['email'], name='user_master_email_19d8d3_idx'),
        ),
    ]
