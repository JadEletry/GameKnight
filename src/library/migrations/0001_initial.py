# Generated by Django 3.2.9 on 2021-11-23 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AuthGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True)),
            ],
            options={
                'db_table': 'auth_group',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroupPermissions',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'auth_group_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthPermission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
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
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('is_superuser', models.IntegerField()),
                ('username', models.CharField(max_length=150, unique=True)),
                ('first_name', models.CharField(max_length=150)),
                ('last_name', models.CharField(max_length=150)),
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
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'auth_user_groups',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserUserPermissions',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'auth_user_user_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Developers',
            fields=[
                ('developerid', models.IntegerField(db_column='DeveloperID', primary_key=True, serialize=False)),
                ('fname', models.CharField(blank=True, db_column='Fname', max_length=45, null=True)),
                ('lname', models.CharField(blank=True, db_column='Lname', max_length=45, null=True)),
                ('sex', models.CharField(blank=True, db_column='Sex', max_length=45, null=True)),
                ('age', models.CharField(blank=True, db_column='Age', max_length=45, null=True)),
            ],
            options={
                'db_table': 'developers',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoAdminLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action_time', models.DateTimeField()),
                ('object_id', models.TextField(blank=True, null=True)),
                ('object_repr', models.CharField(max_length=200)),
                ('action_flag', models.PositiveSmallIntegerField()),
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
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
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
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
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
            name='Game',
            fields=[
                ('gameid', models.IntegerField(db_column='GameID', primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, db_column='Name', max_length=45, null=True)),
                ('releasedate', models.CharField(blank=True, db_column='ReleaseDate', max_length=45, null=True)),
                ('price', models.DecimalField(blank=True, db_column='Price', decimal_places=0, max_digits=3, null=True)),
                ('mode', models.CharField(blank=True, db_column='Mode', max_length=45, null=True)),
            ],
            options={
                'db_table': 'game',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('gname', models.CharField(db_column='GName', max_length=45, primary_key=True, serialize=False)),
                ('genre_tag', models.CharField(blank=True, db_column='Genre/Tag', max_length=45, null=True)),
            ],
            options={
                'db_table': 'genre',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Multiplayer',
            fields=[
                ('players', models.IntegerField(db_column='Players', primary_key=True, serialize=False)),
                ('mode', models.CharField(blank=True, db_column='Mode', max_length=45, null=True)),
                ('gameid', models.IntegerField(blank=True, db_column='GameID', null=True)),
            ],
            options={
                'db_table': 'multiplayer',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Platform',
            fields=[
                ('platformid', models.IntegerField(db_column='PlatformID', primary_key=True, serialize=False)),
                ('system', models.CharField(blank=True, db_column='System', max_length=45, null=True)),
            ],
            options={
                'db_table': 'platform',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('rateno', models.IntegerField(db_column='RateNo', primary_key=True, serialize=False)),
                ('rating', models.DecimalField(blank=True, db_column='Rating', decimal_places=0, max_digits=3, null=True)),
            ],
            options={
                'db_table': 'rating',
                'managed': False,
            },
        ),
    ]