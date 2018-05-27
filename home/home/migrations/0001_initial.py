# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-09-19 15:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Adicaoarestabroom',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('d', models.IntegerField(blank=True, db_column='D', null=True)),
                ('n', models.IntegerField(blank=True, db_column='N', null=True)),
                ('k', models.IntegerField(blank=True, db_column='K', null=True)),
                ('l', models.IntegerField(blank=True, db_column='L', null=True)),
                ('grafooriginal', models.CharField(blank=True, db_column='GrafoOriginal', max_length=12, null=True)),
                ('conectividadealgebrica', models.DecimalField(blank=True, db_column='ConectividadeAlgebrica', decimal_places=12, max_digits=13, null=True)),
                ('aefb1', models.CharField(blank=True, db_column='AEfb1', max_length=7, null=True)),
                ('gefb1', models.DecimalField(blank=True, db_column='GEfb1', decimal_places=12, max_digits=13, null=True)),
                ('aefb2', models.CharField(blank=True, db_column='AEfb2', max_length=8, null=True)),
                ('gefb2', models.DecimalField(blank=True, db_column='GEfb2', decimal_places=17, max_digits=37, null=True)),
                ('aefbt', models.CharField(blank=True, db_column='AefbT', max_length=18, null=True)),
                ('gefb', models.DecimalField(blank=True, db_column='Gefb', decimal_places=12, max_digits=13, null=True)),
                ('aehp1', models.CharField(blank=True, db_column='AEhp1', max_length=7, null=True)),
                ('gehp1', models.DecimalField(blank=True, db_column='GEhp1', decimal_places=12, max_digits=13, null=True)),
                ('aehp2', models.CharField(blank=True, db_column='AEhp2', max_length=7, null=True)),
                ('gehp2', models.DecimalField(blank=True, db_column='GEhp2', decimal_places=12, max_digits=13, null=True)),
                ('aehe1', models.CharField(blank=True, db_column='AEhe1', max_length=7, null=True)),
                ('gehe1', models.DecimalField(blank=True, db_column='GEhe1', decimal_places=12, max_digits=13, null=True)),
                ('aehe2', models.CharField(blank=True, db_column='AEhe2', max_length=7, null=True)),
                ('gehe2', models.DecimalField(blank=True, db_column='GEhe2', decimal_places=12, max_digits=13, null=True)),
                ('melhorheuristica', models.CharField(blank=True, db_column='MelhorHeuristica', max_length=2, null=True)),
            ],
            options={
                'db_table': 'AdicaoArestaBroom',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Adicaoarestadoublebroom',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('d', models.IntegerField(blank=True, db_column='D', null=True)),
                ('n', models.IntegerField(blank=True, db_column='N', null=True)),
                ('k', models.IntegerField(blank=True, db_column='K', null=True)),
                ('l', models.IntegerField(blank=True, db_column='L', null=True)),
                ('grafooriginal', models.CharField(blank=True, db_column='GrafoOriginal', max_length=11, null=True)),
                ('conectividadealgebrica', models.DecimalField(blank=True, db_column='ConectividadeAlgebrica', decimal_places=12, max_digits=13, null=True)),
                ('aefb1', models.CharField(blank=True, db_column='AEfb1', max_length=7, null=True)),
                ('gefb1', models.DecimalField(blank=True, db_column='GEfb1', decimal_places=12, max_digits=13, null=True)),
                ('aefb2', models.CharField(blank=True, db_column='AEfb2', max_length=7, null=True)),
                ('gefb2', models.DecimalField(blank=True, db_column='GEfb2', decimal_places=1, max_digits=20, null=True)),
                ('aefbt', models.CharField(blank=True, db_column='Aefbt', max_length=18, null=True)),
                ('gefb', models.DecimalField(blank=True, db_column='Gefb', decimal_places=12, max_digits=13, null=True)),
                ('aehp1', models.CharField(blank=True, db_column='AEhp1', max_length=7, null=True)),
                ('gehp1', models.DecimalField(blank=True, db_column='GEhp1', decimal_places=12, max_digits=13, null=True)),
                ('aehp2', models.CharField(blank=True, db_column='AEhp2', max_length=7, null=True)),
                ('gehp2', models.DecimalField(blank=True, db_column='GEhp2', decimal_places=12, max_digits=13, null=True)),
                ('aehe1', models.CharField(blank=True, db_column='AEhe1', max_length=7, null=True)),
                ('gehe1', models.DecimalField(blank=True, db_column='GEhe1', decimal_places=12, max_digits=13, null=True)),
                ('aehe2', models.CharField(blank=True, db_column='AEhe2', max_length=19, null=True)),
                ('gehe2', models.CharField(blank=True, db_column='GEhe2', max_length=19, null=True)),
                ('melhorheuristica', models.CharField(blank=True, db_column='MelhorHeuristica', max_length=6, null=True)),
            ],
            options={
                'db_table': 'AdicaoArestaDoubleBroom',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Arvore',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('n', models.IntegerField(blank=True, null=True)),
                ('alfa', models.FloatField(blank=True, null=True)),
                ('y', models.CharField(blank=True, max_length=255, null=True)),
                ('tipo', models.IntegerField(blank=True, null=True)),
                ('diametro', models.IntegerField(blank=True, null=True)),
                ('arestas', models.IntegerField(blank=True, null=True)),
                ('identificacao', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'arvore',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80, unique=True)),
            ],
            options={
                'db_table': 'auth_group',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroupPermissions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_group_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthPermission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('codename', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'auth_permission',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('is_superuser', models.IntegerField()),
                ('username', models.CharField(max_length=150, unique=True)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=254)),
                ('is_staff', models.IntegerField()),
                ('is_active', models.IntegerField()),
                ('date_joined', models.DateTimeField()),
            ],
            options={
                'db_table': 'auth_user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserGroups',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_user_groups',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserUserPermissions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_user_user_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Broom45',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('d', models.IntegerField(blank=True, null=True)),
                ('n', models.IntegerField(blank=True, null=True)),
                ('k', models.IntegerField(blank=True, null=True)),
                ('g', models.CharField(blank=True, db_column='G', max_length=13, null=True)),
                ('l2g', models.CharField(blank=True, db_column='l2G', max_length=5, null=True)),
                ('eph', models.CharField(blank=True, db_column='ePH', max_length=7, null=True)),
                ('l2geph', models.DecimalField(blank=True, db_column='l2GePH', decimal_places=3, max_digits=6, null=True)),
                ('eeh', models.CharField(blank=True, db_column='eEH', max_length=7, null=True)),
                ('l2geeh', models.CharField(blank=True, db_column='l2GeEH', max_length=6, null=True)),
                ('ebf', models.CharField(blank=True, db_column='eBF', max_length=8, null=True)),
            ],
            options={
                'db_table': 'broom45',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Broom89',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('d', models.IntegerField(blank=True, null=True)),
                ('n', models.IntegerField(blank=True, null=True)),
                ('k', models.IntegerField(blank=True, null=True)),
                ('l', models.IntegerField(blank=True, null=True)),
                ('g', models.CharField(blank=True, db_column='G', max_length=14, null=True)),
                ('l2g', models.CharField(blank=True, db_column='l2G', max_length=6, null=True)),
                ('eph', models.CharField(blank=True, db_column='ePH', max_length=7, null=True)),
                ('l2geph', models.CharField(blank=True, db_column='l2GePH', max_length=6, null=True)),
                ('eeh', models.CharField(blank=True, db_column='eEH', max_length=7, null=True)),
                ('l2geeh', models.CharField(blank=True, db_column='l2GeEH', max_length=6, null=True)),
                ('ebf', models.CharField(blank=True, db_column='eBF', max_length=8, null=True)),
            ],
            options={
                'db_table': 'broom89',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoAdminLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action_time', models.DateTimeField()),
                ('object_id', models.TextField(blank=True, null=True)),
                ('object_repr', models.CharField(max_length=200)),
                ('action_flag', models.SmallIntegerField()),
                ('change_message', models.TextField()),
            ],
            options={
                'db_table': 'django_admin_log',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoContentType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_label', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'django_content_type',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoMigrations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('applied', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_migrations',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoSession',
            fields=[
                ('session_key', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('session_data', models.TextField()),
                ('expire_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_session',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Est',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('n', models.BigIntegerField(blank=True, null=True)),
                ('m', models.BigIntegerField(blank=True, null=True)),
                ('ttf', models.BigIntegerField(blank=True, db_column='ttF', null=True)),
                ('ne', models.BigIntegerField(blank=True, db_column='nE', null=True)),
                ('g', models.BigIntegerField(blank=True, db_column='G', null=True)),
                ('itfl', models.BigIntegerField(blank=True, db_column='itFl', null=True)),
                ('uf2', models.BigIntegerField(blank=True, db_column='UF2', null=True)),
                ('ei', models.CharField(blank=True, max_length=63, null=True)),
                ('x1', models.FloatField(blank=True, db_column='X1', null=True)),
                ('ez', models.CharField(blank=True, max_length=63, null=True)),
                ('kig', models.FloatField(blank=True, db_column='KiG', null=True)),
                ('ep', models.CharField(blank=True, db_column='eP', max_length=63, null=True)),
                ('kkg', models.FloatField(blank=True, db_column='KKG', null=True)),
                ('x2', models.FloatField(blank=True, db_column='X2', null=True)),
                ('a2', models.FloatField(blank=True, db_column='A2', null=True)),
            ],
            options={
                'db_table': 'est',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Starlike',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aefb', models.CharField(blank=True, db_column='AEfb', max_length=6, null=True)),
                ('aehe', models.CharField(blank=True, db_column='AEhe', max_length=7, null=True)),
                ('aehe1', models.CharField(blank=True, db_column='AEhe1', max_length=19, null=True)),
                ('aehe2', models.CharField(blank=True, db_column='AEhe2', max_length=19, null=True)),
                ('aehe3', models.CharField(blank=True, db_column='AEhe3', max_length=19, null=True)),
                ('aehe4', models.CharField(blank=True, db_column='AEhe4', max_length=6, null=True)),
                ('aehp', models.CharField(blank=True, db_column='AEhp', max_length=8, null=True)),
                ('aehp1', models.CharField(blank=True, db_column='AEhp1', max_length=8, null=True)),
                ('aehp2', models.CharField(blank=True, db_column='AEhp2', max_length=8, null=True)),
                ('aehp3', models.CharField(blank=True, db_column='AEhp3', max_length=8, null=True)),
                ('aehp4', models.CharField(blank=True, db_column='AEhp4', max_length=6, null=True)),
                ('aefb2', models.CharField(blank=True, db_column='AEfb2', max_length=33, null=True)),
                ('conectividadealgebrica', models.DecimalField(blank=True, db_column='ConectividadeAlgebrica', decimal_places=12, max_digits=32, null=True)),
                ('d', models.IntegerField(blank=True, db_column='D', null=True)),
                ('gefb', models.CharField(blank=True, db_column='GEfb', max_length=20, null=True)),
                ('gefb2', models.CharField(blank=True, db_column='GEfb2', max_length=31, null=True)),
                ('gehe', models.CharField(blank=True, db_column='GEhe', max_length=20, null=True)),
                ('gehe1', models.CharField(blank=True, db_column='GEhe1', max_length=19, null=True)),
                ('gehe2', models.CharField(blank=True, db_column='GEhe2', max_length=19, null=True)),
                ('gehe3', models.CharField(blank=True, db_column='GEhe3', max_length=19, null=True)),
                ('gehe4', models.CharField(blank=True, db_column='GEhe4', max_length=12, null=True)),
                ('gehp', models.CharField(blank=True, db_column='GEhp', max_length=20, null=True)),
                ('gehp1', models.CharField(blank=True, db_column='GEhp1', max_length=31, null=True)),
                ('gehp2', models.CharField(blank=True, db_column='GEhp2', max_length=31, null=True)),
                ('gehp3', models.CharField(blank=True, db_column='GEhp3', max_length=31, null=True)),
                ('gehp4', models.CharField(blank=True, db_column='GEhp4', max_length=12, null=True)),
                ('grafooriginal', models.CharField(blank=True, db_column='GrafoOriginal', max_length=22, null=True)),
                ('graumaximo', models.IntegerField(blank=True, db_column='GrauMaximo', null=True)),
                ('melhorheuristica', models.CharField(blank=True, db_column='MelhorHeuristica', max_length=6, null=True)),
            ],
            options={
                'db_table': 'starlike',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Tables',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, db_column='name', max_length=19, null=True)),
                ('url', models.CharField(blank=True, db_column='url', max_length=19, null=True)),
            ],
            options={
                'db_table': 'Tables',
                'managed': False,
            },
        ),
    ]
