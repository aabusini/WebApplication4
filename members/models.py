from django.db import models

# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

class Centerinfo(models.Model):
    centerid = models.CharField(primary_key=True, db_column='ID', max_length=255, db_collation='Arabic_100_BIN', blank=True)  # Field name made lowercase.
    name = models.CharField(max_length=255, db_collation='Arabic_100_BIN', blank=True, null=True)
    org = models.CharField(max_length=255, db_collation='Arabic_100_BIN', blank=True, null=True)
    centername = models.CharField(max_length=255, db_collation='Arabic_100_BIN', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'centerInfo'


class Data(models.Model):
    objectid = models.CharField(primary_key=True, max_length=255, db_collation='Arabic_100_BIN', blank=True)
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


class Educationlevel(models.Model):
    Eduid = models.IntegerField(db_column='id', primary_key=True)
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


class Users(models.Model):
    userid = models.IntegerField(primary_key=True)
    username = models.CharField(max_length=50, db_collation='Arabic_100_BIN')
    email = models.CharField(max_length=100, db_collation='Arabic_100_BIN')
    password = models.CharField(max_length=100, db_collation='Arabic_100_BIN')
    orgid = models.ForeignKey(Orgdetails, models.DO_NOTHING, db_column='orgid')

    class Meta:
        managed = False
        db_table = 'users'
