from django.db import models

# Create your models here.
class Organizationregister(models.Model):
    organization_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=45)
    email = models.CharField(max_length=45)
    password = models.CharField(max_length=45)
    status = models.CharField(max_length=45)

    class Meta:
        db_table = 'organizationregister'

