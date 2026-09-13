from django.db import models
from register.models import Register
from quiz.models import Quiz
# Create your models here.
class Attend(models.Model):
    attend_id = models.AutoField(primary_key=True)
    # quiz_id = models.IntegerField()
    quiz=models.ForeignKey(Quiz,on_delete=models.CASCADE)
    # register_id = models.IntegerField()
    register=models.ForeignKey(Register,on_delete=models.CASCADE)
    option = models.CharField(max_length=45)

    class Meta:
        db_table = 'attend'


