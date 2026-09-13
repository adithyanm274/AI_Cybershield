from django.db import models

# Create your models here.

class Chat(models.Model):
    chat_id = models.AutoField(primary_key=True)
    message = models.CharField(max_length=100)
    organization_id = models.IntegerField()
    register_id = models.IntegerField()
    sendertype = models.CharField(max_length=30)
    rectype = models.CharField(max_length=30)

    class Meta:
        db_table = 'chat'




