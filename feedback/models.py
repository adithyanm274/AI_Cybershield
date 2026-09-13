from django.db import models
from register.models import Register
# Create your models here.
class Feedback(models.Model):
    feedback_id = models.AutoField(primary_key=True)
    # register_id = models.IntegerField()
    register=models.ForeignKey(Register,on_delete=models.CASCADE)
    date = models.DateField()
    feedback = models.CharField(max_length=500)

    class Meta:
        db_table = 'feedback'
