from django.db import models

# Create your models here.

class Poll(models.Model):
    question = models.TextField()
    datetime = models.DateTimeField(auto_now=True)
    option_one = models.CharField(max_length=56)
    option_two = models.CharField(max_length=56)
    option_three = models.CharField(max_length=56)
    option_four = models.CharField(max_length=56)
    option_one_count = models.IntegerField(default=0)
    option_two_count = models.IntegerField(default=0)
    option_three_count = models.IntegerField(default=0)
    option_four_count = models.IntegerField(default=0)

    def __str__(self):
        return self.question
    