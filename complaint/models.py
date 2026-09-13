from django.db import models
from register.models import Register
# Create your models here.
class Complaint(models.Model):
    complaint_id = models.AutoField(primary_key=True)
    complaint = models.CharField(max_length=500)
    reply = models.CharField(max_length=500)
    # register_id = models.IntegerField()
    register=models.ForeignKey(Register,on_delete=models.CASCADE)
    date = models.DateField()

    class Meta:
        db_table = 'complaint'

