from django.db import models

# Create your models here.
class Quiz(models.Model):
    quiz_id = models.AutoField(primary_key=True)
    question = models.CharField(max_length=45)
    option1 = models.CharField(max_length=45)
    option2 = models.CharField(max_length=45)
    option3 = models.CharField(max_length=45)
    option4 = models.CharField(max_length=45)
    correct_answer = models.CharField(db_column='correct answer', max_length=45)  # Field renamed to remove unsuitable characters.

    class Meta:
        db_table = 'quiz'

