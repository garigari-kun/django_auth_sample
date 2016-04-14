from django.db import models
from user_auth_sample import settings

class Task(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name = 'tasks')
    summary = models.CharField(max_length = 120)
    complete = models.BooleanField(default = False)
    comment = models.CharField(max_length = 512, blank = True)
    done_date = models.DateField(null = True, blank = True)

    def __str__(self):
        return str(self.id) + ': ' + self.summary
