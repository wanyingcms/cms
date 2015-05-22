# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BackuserBackmenu',
            fields=[
                ('id', models.CharField(max_length=32, serialize=False, primary_key=True)),
                ('title', models.CharField(max_length=20)),
                ('url', models.CharField(max_length=100)),
                ('parentid', models.CharField(max_length=32)),
            ],
            options={
                'db_table': 'backuser_backmenu',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='BackuserGroupuser',
            fields=[
                ('id', models.CharField(max_length=32, serialize=False, primary_key=True)),
                ('userid', models.CharField(max_length=32)),
                ('groupid', models.CharField(max_length=32)),
            ],
            options={
                'db_table': 'backuser_groupuser',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='BackuserMenuuser',
            fields=[
                ('id', models.CharField(max_length=32, serialize=False, primary_key=True)),
                ('userid', models.CharField(max_length=32)),
                ('menuid', models.CharField(max_length=32)),
            ],
            options={
                'db_table': 'backuser_menuuser',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='BackuserUserinfo',
            fields=[
                ('id', models.CharField(max_length=32, serialize=False, primary_key=True)),
                ('username', models.CharField(max_length=16)),
                ('comments', models.CharField(max_length=200)),
                ('userpwd', models.CharField(max_length=32)),
                ('logins', models.IntegerField()),
                ('answers', models.IntegerField()),
                ('questions', models.IntegerField()),
                ('lastlogintime', models.DateTimeField()),
                ('createtime', models.DateTimeField()),
                ('createid', models.IntegerField()),
                ('userstatus', models.IntegerField()),
            ],
            options={
                'db_table': 'backuser_userinfo',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='BooksAuthor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=40)),
                ('email', models.CharField(max_length=254)),
            ],
            options={
                'db_table': 'books_author',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='BooksBook',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100)),
                ('publication_date', models.DateField()),
                ('publisher_id', models.IntegerField()),
            ],
            options={
                'db_table': 'books_book',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='BooksBookAuthors',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('book_id', models.IntegerField()),
                ('author_id', models.IntegerField()),
            ],
            options={
                'db_table': 'books_book_authors',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='BooksPublisher',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=60)),
                ('state_province', models.CharField(max_length=30)),
                ('country', models.CharField(max_length=50)),
                ('website', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'books_publisher',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoMigrations',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('app', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('applied', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_migrations',
                'managed': False,
            },
        ),
    ]
