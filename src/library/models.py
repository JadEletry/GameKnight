# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

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
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
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


class Developers(models.Model):
    developerid = models.IntegerField(db_column='DeveloperID', primary_key=True)  # Field name made lowercase.
    fname = models.CharField(db_column='Fname', max_length=45, blank=True, null=True)  # Field name made lowercase.
    lname = models.CharField(db_column='Lname', max_length=45, blank=True, null=True)  # Field name made lowercase.
    sex = models.CharField(db_column='Sex', max_length=45, blank=True, null=True)  # Field name made lowercase.
    age = models.CharField(db_column='Age', max_length=45, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'developers'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
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
    id = models.BigAutoField(primary_key=True)
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


class Game(models.Model):
    gameid = models.IntegerField(db_column='GameID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=45, blank=True, null=True)  # Field name made lowercase.
    releasedate = models.CharField(db_column='ReleaseDate', max_length=45, blank=True, null=True)  # Field name made lowercase.
    price = models.DecimalField(db_column='Price', max_digits=3, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    platformid = models.ForeignKey('Platform', models.DO_NOTHING, db_column='PlatformID', blank=True, null=True)  # Field name made lowercase.
    developerid = models.ForeignKey(Developers, models.DO_NOTHING, db_column='DeveloperID', blank=True, null=True)  # Field name made lowercase.
    gname = models.ForeignKey('Genre', models.DO_NOTHING, db_column='GName', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'game'


class Genre(models.Model):
    gname = models.CharField(db_column='GName', primary_key=True, max_length=45)  # Field name made lowercase.
    genre_tag = models.CharField(db_column='Genre/Tag', max_length=45, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'genre'


class Multiplayer(models.Model):
    players = models.IntegerField(db_column='Players', primary_key=True)  # Field name made lowercase.
    mode = models.CharField(db_column='Mode', max_length=45, blank=True, null=True)  # Field name made lowercase.
    gameid = models.IntegerField(db_column='GameID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'multiplayer'


class Platform(models.Model):
    platformid = models.IntegerField(db_column='PlatformID', primary_key=True)  # Field name made lowercase.
    system = models.CharField(db_column='System', max_length=45, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'platform'


class Rating(models.Model):
    rateno = models.IntegerField(db_column='RateNo', primary_key=True)  # Field name made lowercase.
    gameid = models.ForeignKey(Game, models.DO_NOTHING, db_column='GameID', blank=True, null=True)  # Field name made lowercase.
    rating = models.DecimalField(db_column='Rating', max_digits=3, decimal_places=0, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'rating'