from django.db import models

# Create your models here.
class Credential(models.Model):
    credential_id = models.AutoField(primary_key=True)
    email = models.CharField(max_length=45,null=True,blank=True)
    breach_source = models.CharField(max_length=100,null=True,blank=True)
    breach_date = models.DateField(null=True,blank=True)

    class Meta:
        db_table = 'credential'


from django.db import models

class EmailScan(models.Model):
    scan_id = models.AutoField(primary_key=True)
    email_content = models.TextField()
    risk = models.CharField(max_length=20)
    report = models.TextField()
    recommendation = models.TextField()
    scanned_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "email_scan"