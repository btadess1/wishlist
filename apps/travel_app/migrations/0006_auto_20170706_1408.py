# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-06 18:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('travel_app', '0005_auto_20170706_1232'),
    ]

    operations = [
        migrations.CreateModel(
            name='WishList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='travel_app.User')),
            ],
        ),
        migrations.RemoveField(
            model_name='trip',
            name='user',
        ),
        migrations.RemoveField(
            model_name='joint',
            name='trip',
        ),
        migrations.DeleteModel(
            name='Trip',
        ),
        migrations.AddField(
            model_name='joint',
            name='wishlist',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='travel_app.WishList'),
            preserve_default=False,
        ),
    ]
