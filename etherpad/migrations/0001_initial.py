# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-02-22 11:00
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('blog', '0004_blog_uuid'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='EtherBlog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('etherid', models.TextField()),
                ('groupid', models.TextField(null=True)),
                ('blog', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='ether_blog', to='blog.Blog')),
            ],
        ),
        migrations.CreateModel(
            name='EtherUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_ether_id', models.TextField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ether_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
