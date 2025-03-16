from django.db import models


class Task(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    optional_deadline_datetime = models.DateTimeField(null=True, blank=True)
    is_done = models.BooleanField(default=False)
    tags = models.ManyToManyField("Tag", related_name="tasks")

    def __str__(self):
        return self.content

    class Meta:
        ordering = ["created_at"]


class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
