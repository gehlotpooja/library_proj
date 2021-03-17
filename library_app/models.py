from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Role(models.Model):
    name = models.CharField(max_length=20)

    class Meta:
        db_table = 'tbl_role_table'


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    phone = models.CharField(max_length=20, null=True, blank=True)
    role = models.ForeignKey(Role, on_delete=models.DO_NOTHING)

    class Meta:
        db_table = 'tbl_profile_table'


class Author(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'tbl_author_name'


class Books(models.Model):
    title = models.CharField(max_length=30)
    author = models.ForeignKey(Author,on_delete=models.DO_NOTHING)
    description = models.TextField(null=True, blank=True)

    class Meta:
        db_table = 'tbl_books_table'


class BookIssue(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Books, on_delete=models.CASCADE)
    issue_date = models.DateField(auto_now=True)
    return_date = models.DateField(null=True, blank=True)

    class Meta:
        db_table = 'tbl_book_issue_table'


class ActivityPeriod(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    tz = models.CharField(max_length=30)
    start_time = models.DateTimeField(null=True, blank=True)
    end_time = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = 'tbl_activity_period_table'
