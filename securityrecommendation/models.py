from django.db import models

# Create your models here.

class Securityrecommendation(models.Model):
    security_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=45)
    description = models.CharField(max_length=500)

    class Meta:
        db_table = 'securityrecommendation'

