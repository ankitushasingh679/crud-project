from django.db import models

# Create your models here.
class User(models.Model):
    uname = models.CharField(max_length=50)
    umail = models.EmailField(max_length=50)
    upassword = models.CharField(max_length=50)


    class Meta:
        db_table = 'users'
