from django.db import models
from django.contrib.auth.models import User
# from django.core.validators import MinLengthValidator, RegexValidator
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Note model
class Article(models.Model):
    # Field to store the user's name, maximum length allowed is 100 characters
    title = models.CharField(max_length=100)
    # Field to store the article's content, maximum length allowed is 10000 characters
    body = models.TextField()
    # Field to store the timestamp when the user record was created, automatically set to the current date and time when the user is created
    created_at = models.DateTimeField(auto_now_add=True)
    # Field to store the timestamp of the last update to the user record, automatically set to the current date and time whenever the user record is updated
    updated_at = models.DateTimeField(auto_now=True)
    # Field to store the author of the note, which is a foreign key to the User model, and is required to create a note
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='articles')

    def __str__(self):
        return self.title

class Comment(models.Model):
    # Field to store the comment's body, maximum length allowed is 1000 characters
    body = models.TextField()
    # Field to store the timestamp when the comment was created, automatically set to the current date and time when the comment is created
    created_at = models.DateTimeField(auto_now_add=True)
    # Field to store the timestamp of the last update to the comment, automatically set to the current date and time whenever the comment is updated
    updated_at = models.DateTimeField(auto_now=True)
    # Field to store the author of the comment, which is a foreign key to the User model, and is required to create a comment
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    # Field to store the article of the comment, which is a foreign key to the Article model, and is required to create a comment
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')

    def __str__(self):
        return self.body
