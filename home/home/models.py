# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class Adicaoarestabroom(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    d = models.IntegerField(db_column='D', blank=True, null=True)  # Field name made lowercase.
    n = models.IntegerField(db_column='N', blank=True, null=True)  # Field name made lowercase.
    k = models.IntegerField(db_column='K', blank=True, null=True)  # Field name made lowercase.
    l = models.IntegerField(db_column='L', blank=True, null=True)  # Field name made lowercase.
    grafooriginal = models.CharField(db_column='GrafoOriginal', max_length=12, blank=True, null=True)  # Field name made lowercase.
    conectividadealgebrica = models.DecimalField(db_column='ConectividadeAlgebrica', max_digits=13, decimal_places=12, blank=True, null=True)  # Field name made lowercase.
    aefb1 = models.CharField(db_column='AEfb1', max_length=7, blank=True, null=True)  # Field name made lowercase.
    gefb1 = models.DecimalField(db_column='GEfb1', max_digits=13, decimal_places=12, blank=True, null=True)  # Field name made lowercase.
    aefb2 = models.CharField(db_column='AEfb2', max_length=8, blank=True, null=True)  # Field name made lowercase.
    gefb2 = models.DecimalField(db_column='GEfb2', max_digits=37, decimal_places=17, blank=True, null=True)  # Field name made lowercase.
    aefbt = models.CharField(db_column='AefbT', max_length=18, blank=True, null=True)  # Field name made lowercase.
    gefb = models.DecimalField(db_column='Gefb', max_digits=13, decimal_places=12, blank=True, null=True)  # Field name made lowercase.
    aehp1 = models.CharField(db_column='AEhp1', max_length=7, blank=True, null=True)  # Field name made lowercase.
    gehp1 = models.DecimalField(db_column='GEhp1', max_digits=13, decimal_places=12, blank=True, null=True)  # Field name made lowercase.
    aehp2 = models.CharField(db_column='AEhp2', max_length=7, blank=True, null=True)  # Field name made lowercase.
    gehp2 = models.DecimalField(db_column='GEhp2', max_digits=13, decimal_places=12, blank=True, null=True)  # Field name made lowercase.
    aehe1 = models.CharField(db_column='AEhe1', max_length=7, blank=True, null=True)  # Field name made lowercase.
    gehe1 = models.DecimalField(db_column='GEhe1', max_digits=13, decimal_places=12, blank=True, null=True)  # Field name made lowercase.
    aehe2 = models.CharField(db_column='AEhe2', max_length=7, blank=True, null=True)  # Field name made lowercase.
    gehe2 = models.DecimalField(db_column='GEhe2', max_digits=13, decimal_places=12, blank=True, null=True)  # Field name made lowercase.
    melhorheuristica = models.CharField(db_column='MelhorHeuristica', max_length=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AdicaoArestaBroom'


class Adicaoarestadoublebroom(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    d = models.IntegerField(db_column='D', blank=True, null=True)  # Field name made lowercase.
    n = models.IntegerField(db_column='N', blank=True, null=True)  # Field name made lowercase.
    k = models.IntegerField(db_column='K', blank=True, null=True)  # Field name made lowercase.
    l = models.IntegerField(db_column='L', blank=True, null=True)  # Field name made lowercase.
    grafooriginal = models.CharField(db_column='GrafoOriginal', max_length=11, blank=True, null=True)  # Field name made lowercase.
    conectividadealgebrica = models.DecimalField(db_column='ConectividadeAlgebrica', max_digits=13, decimal_places=12, blank=True, null=True)  # Field name made lowercase.
    aefb1 = models.CharField(db_column='AEfb1', max_length=7, blank=True, null=True)  # Field name made lowercase.
    gefb1 = models.DecimalField(db_column='GEfb1', max_digits=13, decimal_places=12, blank=True, null=True)  # Field name made lowercase.
    aefb2 = models.CharField(db_column='AEfb2', max_length=7, blank=True, null=True)  # Field name made lowercase.
    gefb2 = models.DecimalField(db_column='GEfb2', max_digits=20, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    aefbt = models.CharField(db_column='Aefbt', max_length=18, blank=True, null=True)  # Field name made lowercase.
    gefb = models.DecimalField(db_column='Gefb', max_digits=13, decimal_places=12, blank=True, null=True)  # Field name made lowercase.
    aehp1 = models.CharField(db_column='AEhp1', max_length=7, blank=True, null=True)  # Field name made lowercase.
    gehp1 = models.DecimalField(db_column='GEhp1', max_digits=13, decimal_places=12, blank=True, null=True)  # Field name made lowercase.
    aehp2 = models.CharField(db_column='AEhp2', max_length=7, blank=True, null=True)  # Field name made lowercase.
    gehp2 = models.DecimalField(db_column='GEhp2', max_digits=13, decimal_places=12, blank=True, null=True)  # Field name made lowercase.
    aehe1 = models.CharField(db_column='AEhe1', max_length=7, blank=True, null=True)  # Field name made lowercase.
    gehe1 = models.DecimalField(db_column='GEhe1', max_digits=13, decimal_places=12, blank=True, null=True)  # Field name made lowercase.
    aehe2 = models.CharField(db_column='AEhe2', max_length=19, blank=True, null=True)  # Field name made lowercase.
    gehe2 = models.CharField(db_column='GEhe2', max_length=19, blank=True, null=True)  # Field name made lowercase.
    melhorheuristica = models.CharField(db_column='MelhorHeuristica', max_length=6, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AdicaoArestaDoubleBroom'


class Arvore(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    n = models.IntegerField(blank=True, null=True)
    alfa = models.FloatField(blank=True, null=True)
    y = models.CharField(max_length=255, blank=True, null=True)
    tipo = models.IntegerField(blank=True, null=True)
    diametro = models.IntegerField(blank=True, null=True)
    arestas = models.IntegerField(blank=True, null=True)
    identificacao = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'arvore'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Broom45(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    d = models.IntegerField(blank=True, null=True)
    n = models.IntegerField(blank=True, null=True)
    k = models.IntegerField(blank=True, null=True)
    g = models.CharField(db_column='G', max_length=13, blank=True, null=True)  # Field name made lowercase.
    l2g = models.CharField(db_column='l2G', max_length=5, blank=True, null=True)  # Field name made lowercase.
    eph = models.CharField(db_column='ePH', max_length=7, blank=True, null=True)  # Field name made lowercase.
    l2geph = models.DecimalField(db_column='l2GePH', max_digits=6, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    eeh = models.CharField(db_column='eEH', max_length=7, blank=True, null=True)  # Field name made lowercase.
    l2geeh = models.CharField(db_column='l2GeEH', max_length=6, blank=True, null=True)  # Field name made lowercase.
    ebf = models.CharField(db_column='eBF', max_length=8, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'broom45'


class Broom89(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    d = models.IntegerField(blank=True, null=True)
    n = models.IntegerField(blank=True, null=True)
    k = models.IntegerField(blank=True, null=True)
    l = models.IntegerField(blank=True, null=True)
    g = models.CharField(db_column='G', max_length=14, blank=True, null=True)  # Field name made lowercase.
    l2g = models.CharField(db_column='l2G', max_length=6, blank=True, null=True)  # Field name made lowercase.
    eph = models.CharField(db_column='ePH', max_length=7, blank=True, null=True)  # Field name made lowercase.
    l2geph = models.CharField(db_column='l2GePH', max_length=6, blank=True, null=True)  # Field name made lowercase.
    eeh = models.CharField(db_column='eEH', max_length=7, blank=True, null=True)  # Field name made lowercase.
    l2geeh = models.CharField(db_column='l2GeEH', max_length=6, blank=True, null=True)  # Field name made lowercase.
    ebf = models.CharField(db_column='eBF', max_length=8, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'broom89'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Est(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    #id = models.BigIntegerField(blank=True, null=True)
    n = models.BigIntegerField(blank=True, null=True)
    m = models.BigIntegerField(blank=True, null=True)
    ttf = models.BigIntegerField(db_column='ttF', blank=True, null=True)  # Field name made lowercase.
    ne = models.BigIntegerField(db_column='nE', blank=True, null=True)  # Field name made lowercase.
    g = models.BigIntegerField(db_column='G', blank=True, null=True)  # Field name made lowercase.
    itfl = models.BigIntegerField(db_column='itFl', blank=True, null=True)  # Field name made lowercase.
    uf2 = models.BigIntegerField(db_column='UF2', blank=True, null=True)  # Field name made lowercase.
    ei = models.CharField(max_length=63, blank=True, null=True)
    x1 = models.FloatField(db_column='X1', blank=True, null=True)  # Field name made lowercase.
    ez = models.CharField(max_length=63, blank=True, null=True)
    kig = models.FloatField(db_column='KiG', blank=True, null=True)  # Field name made lowercase.
    ep = models.CharField(db_column='eP', max_length=63, blank=True, null=True)  # Field name made lowercase.
    kkg = models.FloatField(db_column='KKG', blank=True, null=True)  # Field name made lowercase.
    x2 = models.FloatField(db_column='X2', blank=True, null=True)  # Field name made lowercase.
    a2 = models.FloatField(db_column='A2', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'est'


class Starlike(models.Model):
    aefb = models.CharField(db_column='AEfb', max_length=6, blank=True, null=True)  # Field name made lowercase.
    aehe = models.CharField(db_column='AEhe', max_length=7, blank=True, null=True)  # Field name made lowercase.
    aehe1 = models.CharField(db_column='AEhe1', max_length=19, blank=True, null=True)  # Field name made lowercase.
    aehe2 = models.CharField(db_column='AEhe2', max_length=19, blank=True, null=True)  # Field name made lowercase.
    aehe3 = models.CharField(db_column='AEhe3', max_length=19, blank=True, null=True)  # Field name made lowercase.
    aehe4 = models.CharField(db_column='AEhe4', max_length=6, blank=True, null=True)  # Field name made lowercase.
    aehp = models.CharField(db_column='AEhp', max_length=8, blank=True, null=True)  # Field name made lowercase.
    aehp1 = models.CharField(db_column='AEhp1', max_length=8, blank=True, null=True)  # Field name made lowercase.
    aehp2 = models.CharField(db_column='AEhp2', max_length=8, blank=True, null=True)  # Field name made lowercase.
    aehp3 = models.CharField(db_column='AEhp3', max_length=8, blank=True, null=True)  # Field name made lowercase.
    aehp4 = models.CharField(db_column='AEhp4', max_length=6, blank=True, null=True)  # Field name made lowercase.
    aefb2 = models.CharField(db_column='AEfb2', max_length=33, blank=True, null=True)  # Field name made lowercase.
    conectividadealgebrica = models.DecimalField(db_column='ConectividadeAlgebrica', max_digits=32, decimal_places=12, blank=True, null=True)  # Field name made lowercase.
    d = models.IntegerField(db_column='D', blank=True, null=True)  # Field name made lowercase.
    gefb = models.CharField(db_column='GEfb', max_length=20, blank=True, null=True)  # Field name made lowercase.
    gefb2 = models.CharField(db_column='GEfb2', max_length=31, blank=True, null=True)  # Field name made lowercase.
    gehe = models.CharField(db_column='GEhe', max_length=20, blank=True, null=True)  # Field name made lowercase.
    gehe1 = models.CharField(db_column='GEhe1', max_length=19, blank=True, null=True)  # Field name made lowercase.
    gehe2 = models.CharField(db_column='GEhe2', max_length=19, blank=True, null=True)  # Field name made lowercase.
    gehe3 = models.CharField(db_column='GEhe3', max_length=19, blank=True, null=True)  # Field name made lowercase.
    gehe4 = models.CharField(db_column='GEhe4', max_length=12, blank=True, null=True)  # Field name made lowercase.
    gehp = models.CharField(db_column='GEhp', max_length=20, blank=True, null=True)  # Field name made lowercase.
    gehp1 = models.CharField(db_column='GEhp1', max_length=31, blank=True, null=True)  # Field name made lowercase.
    gehp2 = models.CharField(db_column='GEhp2', max_length=31, blank=True, null=True)  # Field name made lowercase.
    gehp3 = models.CharField(db_column='GEhp3', max_length=31, blank=True, null=True)  # Field name made lowercase.
    gehp4 = models.CharField(db_column='GEhp4', max_length=12, blank=True, null=True)  # Field name made lowercase.
    grafooriginal = models.CharField(db_column='GrafoOriginal', max_length=22, blank=True, null=True)  # Field name made lowercase.
    graumaximo = models.IntegerField(db_column='GrauMaximo', blank=True, null=True)  # Field name made lowercase.
    melhorheuristica = models.CharField(db_column='MelhorHeuristica', max_length=6, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'starlike'

class Tables(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='name', max_length=19, blank=True, null=True)  # Field name made lowercase.
    url = models.CharField(db_column='url', max_length=19, blank=True, null=True)  # Field name made lowercase.
    file = models.CharField(db_column='file', max_length=6, blank=True, null=True)  # Field name made lowercase.
    #file = models.FileField(upload_to= 'class')
    class Meta:
        managed = False
        db_table = 'Tables'
