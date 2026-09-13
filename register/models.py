from django.db import models

# Create your models here.
class Register(models.Model):
    register_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=45)
    email = models.CharField(max_length=45)
    password = models.CharField(max_length=45)
    status = models.CharField(max_length=45)

    class Meta:
        db_table = 'register'
