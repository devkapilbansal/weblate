# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-17 10:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('trans', '0075_auto_20170215_1750'),
        ('auth', '0008_alter_user_username_max_length'),
        ('lang', '0004_auto_20161222_1459'),
    ]

    operations = [
        migrations.CreateModel(
            name='GroupACL',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('groups', models.ManyToManyField(to='auth.Group')),
                ('language', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='lang.Language')),
                ('project', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='trans.Project')),
                ('subproject', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='trans.SubProject')),
            ],
            options={
                'verbose_name': 'Group ACL',
                'verbose_name_plural': 'Group ACLs',
            },
        ),
        migrations.AlterUniqueTogether(
            name='groupacl',
            unique_together=set([('project', 'subproject', 'language')]),
        ),
    ]
