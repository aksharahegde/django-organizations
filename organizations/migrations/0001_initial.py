# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-05-10 14:24
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import organizations.base
import organizations.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='The name of the organization', max_length=200)),
                ('is_active', models.BooleanField(default=True)),
                ('created', organizations.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False)),
                ('modified', organizations.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False)),
                ('slug', organizations.fields.SlugField(blank=True, editable=False, help_text='The name in all lowercase, suitable for URL identification', max_length=200, populate_from=b'name', unique=True)),
            ],
            options={
                'ordering': ['name'],
                'abstract': False,
                'verbose_name': 'organization',
                'verbose_name_plural': 'organizations',
            },
            bases=(organizations.base.UnicodeMixin, models.Model),
        ),
        migrations.CreateModel(
            name='OrganizationOwner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', organizations.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False)),
                ('modified', organizations.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False)),
                ('organization', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='owner', to='organizations.Organization')),
            ],
            options={
                'abstract': False,
                'verbose_name': 'organization owner',
                'verbose_name_plural': 'organization owners',
            },
            bases=(organizations.base.UnicodeMixin, models.Model),
        ),
        migrations.CreateModel(
            name='OrganizationUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', organizations.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False)),
                ('modified', organizations.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False)),
                ('is_admin', models.BooleanField(default=False)),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='organization_users', to='organizations.Organization')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='organizations_organizationuser', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['organization', 'user'],
                'abstract': False,
                'verbose_name_plural': 'organization users',
                'verbose_name': 'organization user',
            },
            bases=(organizations.base.UnicodeMixin, models.Model),
        ),
        migrations.AddField(
            model_name='organizationowner',
            name='organization_user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='organizations.OrganizationUser'),
        ),
        migrations.AddField(
            model_name='organization',
            name='users',
            field=models.ManyToManyField(related_name='organizations_organization', through='organizations.OrganizationUser', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterUniqueTogether(
            name='organizationuser',
            unique_together=set([('user', 'organization')]),
        ),
    ]
