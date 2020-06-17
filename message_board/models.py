from django.db import models


class Post(models.Model):
    title = models.TextField(max_length=50)
    text = models.TextField()

    def __str__(self):
        return self.text
