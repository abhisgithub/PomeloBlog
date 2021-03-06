# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-01-08 11:02
from __future__ import unicode_literals

import blog.models
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
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('body', models.TextField(null=True)),
                ('image', models.ImageField(null=True, upload_to=blog.models.get_file_path)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('published_on', models.DateTimeField(null=True)),
                ('views', models.PositiveIntegerField(default=0)),
                ('status', models.CharField(choices=[('Draft', 'Draft'), ('Publish', 'Publish')], max_length=50)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blog_author', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
