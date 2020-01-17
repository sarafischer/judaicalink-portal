from django.db import models
from datetime import datetime
# Create your models here.

class Dataset(models.Model):
    name = models.TextField()


class ThreadTask(models.Model):
    name = models.TextField()
    is_done = models.BooleanField(blank=False, default=False)
    log_text = models.TextField()

    def done(self):
        self.is_done = True
        self.save()

    def log(self, message):
        self.refresh_from_db()
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
        self.log_text += '\n' + timestamp + ": " + message
        self.save() 

    def last_log(self):
        msgs = self.log_text.split('\n')
        for i in range(len(msgs) - 1, 0, -1):
            if msgs[i].strip():
                return msgs[i]
        return ""

    def __str__(self):
        return "{}".format(self.name)