# Generated by Django 4.0.4 on 2022-05-01 15:01

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
                ('name', models.CharField(db_collation='Arabic_100_BIN', max_length=150, unique=True)),
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
                ('name', models.CharField(db_collation='Arabic_100_BIN', max_length=255)),
                ('codename', models.CharField(db_collation='Arabic_100_BIN', max_length=100)),
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
                ('password', models.CharField(db_collation='Arabic_100_BIN', max_length=128)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('is_superuser', models.BooleanField()),
                ('username', models.CharField(db_collation='Arabic_100_BIN', max_length=150, unique=True)),
                ('first_name', models.CharField(db_collation='Arabic_100_BIN', max_length=150)),
                ('last_name', models.CharField(db_collation='Arabic_100_BIN', max_length=150)),
                ('email', models.CharField(db_collation='Arabic_100_BIN', max_length=254)),
                ('is_staff', models.BooleanField()),
                ('is_active', models.BooleanField()),
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
            name='Centerinfo',
            fields=[
                ('id', models.CharField(blank=True, db_collation='Arabic_100_BIN', db_column='ID', max_length=255, primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, db_collation='Arabic_100_BIN', max_length=255, null=True)),
                ('org', models.CharField(blank=True, db_collation='Arabic_100_BIN', max_length=255, null=True)),
                ('centername', models.CharField(blank=True, db_collation='Arabic_100_BIN', max_length=255, null=True)),
            ],
            options={
                'db_table': 'centerInfo',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('objectid', models.CharField(blank=True, db_collation='Arabic_100_BIN', max_length=255, null=True)),
                ('first_name', models.CharField(blank=True, db_collation='Arabic_100_BIN', max_length=255, null=True)),
                ('nationality', models.CharField(blank=True, db_collation='Arabic_100_BIN', max_length=255, null=True)),
                ('unilevel', models.CharField(blank=True, db_collation='Arabic_100_BIN', max_length=255, null=True)),
                ('ben_id', models.CharField(blank=True, db_collation='Arabic_100_BIN', max_length=255, null=True)),
                ('fisrt_phone', models.CharField(blank=True, db_collation='Arabic_100_BIN', max_length=255, null=True)),
                ('second_phone', models.CharField(blank=True, db_collation='Arabic_100_BIN', max_length=255, null=True)),
                ('gov', models.CharField(blank=True, db_collation='Arabic_100_BIN', max_length=255, null=True)),
                ('org_name', models.CharField(blank=True, db_collation='Arabic_100_BIN', max_length=255, null=True)),
                ('interested_in_working', models.CharField(blank=True, db_collation='Arabic_100_BIN', max_length=255, null=True)),
                ('benefited_from_makani', models.CharField(blank=True, db_collation='Arabic_100_BIN', max_length=255, null=True)),
                ('vaccinated', models.CharField(blank=True, db_collation='Arabic_100_BIN', max_length=255, null=True)),
                ('courses', models.CharField(blank=True, db_collation='Arabic_100_BIN', max_length=255, null=True)),
                ('created_date', models.DateTimeField(blank=True, null=True)),
                ('lastdegree', models.CharField(blank=True, db_collation='Arabic_100_BIN', max_length=255, null=True)),
                ('readw', models.CharField(blank=True, db_collation='Arabic_100_BIN', max_length=255, null=True)),
                ('other_ben', models.CharField(blank=True, db_collation='Arabic_100_BIN', max_length=255, null=True)),
                ('other_ben_id', models.CharField(blank=True, db_collation='Arabic_100_BIN', max_length=255, null=True)),
                ('c1', models.CharField(blank=True, db_collation='Arabic_100_BIN', max_length=255, null=True)),
                ('c2', models.CharField(blank=True, db_collation='Arabic_100_BIN', max_length=255, null=True)),
                ('c3', models.CharField(blank=True, db_collation='Arabic_100_BIN', max_length=255, null=True)),
                ('c4', models.CharField(blank=True, db_collation='Arabic_100_BIN', max_length=255, null=True)),
                ('c5', models.CharField(blank=True, db_collation='Arabic_100_BIN', max_length=255, null=True)),
                ('c6', models.CharField(blank=True, db_collation='Arabic_100_BIN', max_length=255, null=True)),
                ('c7', models.CharField(blank=True, db_collation='Arabic_100_BIN', max_length=255, null=True)),
                ('c8', models.CharField(blank=True, db_collation='Arabic_100_BIN', max_length=255, null=True)),
                ('c9', models.CharField(blank=True, db_collation='Arabic_100_BIN', max_length=255, null=True)),
                ('c10', models.CharField(blank=True, db_collation='Arabic_100_BIN', max_length=255, null=True)),
                ('c11', models.CharField(blank=True, db_collation='Arabic_100_BIN', max_length=255, null=True)),
                ('c12', models.CharField(blank=True, db_collation='Arabic_100_BIN', max_length=255, null=True)),
                ('c13', models.CharField(blank=True, db_collation='Arabic_100_BIN', max_length=255, null=True)),
                ('c14', models.CharField(blank=True, db_collation='Arabic_100_BIN', max_length=255, null=True)),
                ('c15', models.CharField(blank=True, db_collation='Arabic_100_BIN', max_length=255, null=True)),
                ('c16', models.CharField(blank=True, db_collation='Arabic_100_BIN', max_length=255, null=True)),
                ('c17', models.CharField(blank=True, db_collation='Arabic_100_BIN', max_length=255, null=True)),
            ],
            options={
                'db_table': 'data',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoAdminLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action_time', models.DateTimeField()),
                ('object_id', models.TextField(blank=True, db_collation='Arabic_100_BIN', null=True)),
                ('object_repr', models.CharField(db_collation='Arabic_100_BIN', max_length=200)),
                ('action_flag', models.SmallIntegerField()),
                ('change_message', models.TextField(db_collation='Arabic_100_BIN')),
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
                ('app_label', models.CharField(db_collation='Arabic_100_BIN', max_length=100)),
                ('model', models.CharField(db_collation='Arabic_100_BIN', max_length=100)),
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
                ('app', models.CharField(db_collation='Arabic_100_BIN', max_length=255)),
                ('name', models.CharField(db_collation='Arabic_100_BIN', max_length=255)),
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
                ('session_key', models.CharField(db_collation='Arabic_100_BIN', max_length=40, primary_key=True, serialize=False)),
                ('session_data', models.TextField(db_collation='Arabic_100_BIN')),
                ('expire_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_session',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Educationlevel',
            fields=[
                ('id', models.IntegerField(blank=True, primary_key=True, serialize=False)),
                ('eduname', models.CharField(blank=True, db_collation='Arabic_100_BIN', max_length=255, null=True)),
            ],
            options={
                'db_table': 'educationlevel',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Orgdetails',
            fields=[
                ('orgid', models.IntegerField(primary_key=True, serialize=False)),
                ('orgname', models.CharField(db_collation='Arabic_100_BIN', max_length=100)),
            ],
            options={
                'db_table': 'orgdetails',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Sysdiagrams',
            fields=[
                ('name', models.CharField(db_collation='Arabic_100_BIN', max_length=128)),
                ('principal_id', models.IntegerField()),
                ('diagram_id', models.AutoField(primary_key=True, serialize=False)),
                ('version', models.IntegerField(blank=True, null=True)),
                ('definition', models.BinaryField(blank=True, max_length='max', null=True)),
            ],
            options={
                'db_table': 'sysdiagrams',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('userid', models.IntegerField(primary_key=True, serialize=False)),
                ('username', models.CharField(db_collation='Arabic_100_BIN', max_length=50)),
                ('email', models.CharField(db_collation='Arabic_100_BIN', max_length=100)),
                ('password', models.CharField(db_collation='Arabic_100_BIN', max_length=100)),
            ],
            options={
                'db_table': 'users',
                'managed': False,
            },
        ),
    ]
