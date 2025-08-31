from django.db import models
from django.utils import timezone
import uuid

class Question(models.Model):
    text = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)

class Answer(models.Model):
    question = models.ForeignKey(
        Question,
        related_name="answers",
        on_delete=models.CASCADE,
    )
    user_id = models.UUIDField(default=uuid.uuid4, editable=False)
    text = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)