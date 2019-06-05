import datetime

from django.db import models


class TodoList(models.Model):
    title = models.CharField(max_length = 250)
    done = models.BooleanField(default = False)
    author_ip = models.CharField(blank = True, max_length = 25)
    created_date = models.CharField(default = datetime.datetime.utcnow().strftime("%Y-%m-%d, %H:%M:%S"),
                                    max_length = 50)
    done_date = models.CharField(blank = True, null = True, max_length = 50)

    def save(self, *args, **kwargs):

        if self.done is True and not self.done_date:
            self.done_date = datetime.datetime.utcnow().strftime("%Y-%m-%d, %H:%M:%S")

        if self.pk is not None:
            orig = TodoList.objects.get(pk = self.pk)
            if orig.done is True and self.done is False:
                self.done_date = None

        super(TodoList, self).save(*args, **kwargs)
