# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150, db_collation='Arabic_100_BIN')

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255, db_collation='Arabic_100_BIN')
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100, db_collation='Arabic_100_BIN')

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128, db_collation='Arabic_100_BIN')
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150, db_collation='Arabic_100_BIN')
    first_name = models.CharField(max_length=150, db_collation='Arabic_100_BIN')
    last_name = models.CharField(max_length=150, db_collation='Arabic_100_BIN')
    email = models.CharField(max_length=254, db_collation='Arabic_100_BIN')
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Centerinfo(models.Model):
    id = models.CharField(db_column='ID', max_length=255, db_collation='Arabic_100_BIN', blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(max_length=255, db_collation='Arabic_100_BIN', blank=True, null=True)
    org = models.CharField(max_length=255, db_collation='Arabic_100_BIN', blank=True, null=True)
    centername = models.CharField(max_length=255, db_collation='Arabic_100_BIN', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'centerInfo'


class Data(models.Model):
    objectid = models.CharField(max_length=255, db_collation='Arabic_100_BIN', blank=True, null=True)
    first_name = models.CharField(max_length=255, db_collation='Arabic_100_BIN', blank=True, null=True)
    nationality = models.CharField(max_length=255, db_collation='Arabic_100_BIN', blank=True, null=True)
    unilevel = models.CharField(max_length=255, db_collation='Arabic_100_BIN', blank=True, null=True)
    ben_id = models.CharField(max_length=255, db_collation='Arabic_100_BIN', blank=True, null=True)
    fisrt_phone = models.CharField(max_length=255, db_collation='Arabic_100_BIN', blank=True, null=True)
    second_phone = models.CharField(max_length=255, db_collation='Arabic_100_BIN', blank=True, null=True)
    gov = models.CharField(max_length=255, db_collation='Arabic_100_BIN', blank=True, null=True)
    org_name = models.CharField(max_length=255, db_collation='Arabic_100_BIN', blank=True, null=True)
    interested_in_working = models.CharField(max_length=255, db_collation='Arabic_100_BIN', blank=True, null=True)
    benefited_from_makani = models.CharField(max_length=255, db_collation='Arabic_100_BIN', blank=True, null=True)
    vaccinated = models.CharField(max_length=255, db_collation='Arabic_100_BIN', blank=True, null=True)
    courses = models.CharField(max_length=255, db_collation='Arabic_100_BIN', blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)
    lastdegree = models.CharField(max_length=255, db_collation='Arabic_100_BIN', blank=True, null=True)
    readw = models.CharField(max_length=255, db_collation='Arabic_100_BIN', blank=True, null=True)
    other_ben = models.CharField(max_length=255, db_collation='Arabic_100_BIN', blank=True, null=True)
    other_ben_id = models.CharField(max_length=255, db_collation='Arabic_100_BIN', blank=True, null=True)
    c1 = models.CharField(max_length=255, db_collation='Arabic_100_BIN', blank=True, null=True)
    c2 = models.CharField(max_length=255, db_collation='Arabic_100_BIN', blank=True, null=True)
    c3 = models.CharField(max_length=255, db_collation='Arabic_100_BIN', blank=True, null=True)
    c4 = models.CharField(max_length=255, db_collation='Arabic_100_BIN', blank=True, null=True)
    c5 = models.CharField(max_length=255, db_collation='Arabic_100_BIN', blank=True, null=True)
    c6 = models.CharField(max_length=255, db_collation='Arabic_100_BIN', blank=True, null=True)
    c7 = models.CharField(max_length=255, db_collation='Arabic_100_BIN', blank=True, null=True)
    c8 = models.CharField(max_length=255, db_collation='Arabic_100_BIN', blank=True, null=True)
    c9 = models.CharField(max_length=255, db_collation='Arabic_100_BIN', blank=True, null=True)
    c10 = models.CharField(max_length=255, db_collation='Arabic_100_BIN', blank=True, null=True)
    c11 = models.CharField(max_length=255, db_collation='Arabic_100_BIN', blank=True, null=True)
    c12 = models.CharField(max_length=255, db_collation='Arabic_100_BIN', blank=True, null=True)
    c13 = models.CharField(max_length=255, db_collation='Arabic_100_BIN', blank=True, null=True)
    c14 = models.CharField(max_length=255, db_collation='Arabic_100_BIN', blank=True, null=True)
    c15 = models.CharField(max_length=255, db_collation='Arabic_100_BIN', blank=True, null=True)
    c16 = models.CharField(max_length=255, db_collation='Arabic_100_BIN', blank=True, null=True)
    c17 = models.CharField(max_length=255, db_collation='Arabic_100_BIN', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'data'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(db_collation='Arabic_100_BIN', blank=True, null=True)
    object_repr = models.CharField(max_length=200, db_collation='Arabic_100_BIN')
    action_flag = models.SmallIntegerField()
    change_message = models.TextField(db_collation='Arabic_100_BIN')
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100, db_collation='Arabic_100_BIN')
    model = models.CharField(max_length=100, db_collation='Arabic_100_BIN')

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255, db_collation='Arabic_100_BIN')
    name = models.CharField(max_length=255, db_collation='Arabic_100_BIN')
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40, db_collation='Arabic_100_BIN')
    session_data = models.TextField(db_collation='Arabic_100_BIN')
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Educationlevel(models.Model):
    id = models.IntegerField(blank=True, null=True)
    eduname = models.CharField(max_length=255, db_collation='Arabic_100_BIN', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'educationlevel'


class Orgdetails(models.Model):
    orgid = models.IntegerField(primary_key=True)
    orgname = models.CharField(max_length=100, db_collation='Arabic_100_BIN')

    class Meta:
        managed = False
        db_table = 'orgdetails'


class Sysdiagrams(models.Model):
    name = models.CharField(max_length=128, db_collation='Arabic_100_BIN')
    principal_id = models.IntegerField()
    diagram_id = models.AutoField(primary_key=True)
    version = models.IntegerField(blank=True, null=True)
    definition = models.BinaryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sysdiagrams'
        unique_together = (('principal_id', 'name'),)


class Users(models.Model):
    userid = models.IntegerField(primary_key=True)
    username = models.CharField(max_length=50, db_collation='Arabic_100_BIN')
    email = models.CharField(max_length=100, db_collation='Arabic_100_BIN')
    password = models.CharField(max_length=100, db_collation='Arabic_100_BIN')
    orgid = models.ForeignKey(Orgdetails, models.DO_NOTHING, db_column='orgid')

    class Meta:
        managed = False
        db_table = 'users'
