#coding:utf-8
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals

from django.db import models


class BackuserBackmenu(models.Model):
    id = models.CharField(primary_key=True, max_length=32)
    title = models.CharField(max_length=20)
    url = models.CharField(max_length=100)
    parentid = models.CharField(max_length=32)

    class Meta:
        managed = False
        db_table = 'backuser_backmenu'


class BackuserGroupuser(models.Model):
    id = models.CharField(primary_key=True, max_length=32)
    userid = models.CharField(max_length=32)
    groupid = models.CharField(max_length=32)

    class Meta:
        managed = False
        db_table = 'backuser_groupuser'


class BackuserMenuuser(models.Model):
    id = models.CharField(primary_key=True, max_length=32)
    userid = models.CharField(max_length=32)
    menuid = models.CharField(max_length=32)

    class Meta:
        managed = False
        db_table = 'backuser_menuuser'


class BackuserUserinfo(models.Model):
    id = models.CharField(primary_key=True, max_length=32)
    username = models.CharField(max_length=16)
    comments = models.CharField(max_length=200)
    userpwd = models.CharField(max_length=32)
    logins = models.IntegerField()
    answers = models.IntegerField()
    questions = models.IntegerField()
    lastlogintime = models.DateTimeField()
    createtime = models.DateTimeField()
    createid = models.IntegerField()
    userstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'backuser_userinfo'


#class BooksAuthor(models.Model):
#    first_name = models.CharField(max_length=30)
#    last_name = models.CharField(max_length=40)
#    email = models.CharField(max_length=254)

#    class Meta:
#        managed = False
#        db_table = 'books_author'


#class BooksBook(models.Model):
#    title = models.CharField(max_length=100)
#    publication_date = models.DateField()
#    publisher_id = models.IntegerField()

 #   class Meta:
 #       managed = False
 #       db_table = 'books_book'


#class BooksBookAuthors(models.Model):
#    book_id = models.IntegerField()
#    author_id = models.IntegerField()

#    class Meta:
#        managed = False
#        db_table = 'books_book_authors'
#        unique_together = (('book_id', 'author_id'),)


#class BooksPublisher(models.Model):
#    name = models.CharField(max_length=30)
#    address = models.CharField(max_length=50)
#    city = models.CharField(max_length=60)
#    state_province = models.CharField(max_length=30)
#    country = models.CharField(max_length=50)
#    website = models.CharField(max_length=200)

#    class Meta:
 #       managed = False
 #       db_table = 'books_publisher'


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'
