from django.db import models
from dailyLog.config.base import AUTH_USER_MODEL

FIELD_CHOICES = [('BooleanField', 'Yes / No'), ('IntegerField', 'Numeric value')]
DAY_CHOICES = sorted([(item, item) for item in range(0, 8)])


# Create your models here.
class Habit(models.Model):
    owner = models.ForeignKey(AUTH_USER_MODEL, related_name='habits', on_delete=models.CASCADE)
    title = models.CharField(max_length=100, blank=False, default='')
    display_type = models.CharField(choices=FIELD_CHOICES, max_length=100, default="BooleanField")
    weekly_goal = models.IntegerField(choices=DAY_CHOICES, default=7)

    def __str__(self):
        return self.title


class Log(models.Model):
    date = models.DateField()
    score = models.IntegerField()
    habit = models.ForeignKey(Habit, related_name='logs', on_delete=models.CASCADE)

    def __str__(self):
        return self.habit.title + ": " + str(self.date) + " | " + str(self.score)

