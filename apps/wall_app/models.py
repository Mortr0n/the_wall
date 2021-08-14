from django.db import models
from apps.login_registration_app.models import User

class Message(models.Model):
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user_id = models.ForeignKey(User, related_name='user_messages', on_delete=models.CASCADE)
    # message_comments
    # user_comments


class Comment(models.Model):
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    message_id = models.ForeignKey(Message, related_name='message_comments', on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, related_name='user_comments', on_delete=models.CASCADE)