from django.db import models

# Create your models here.
class User(models.Model):
    # Field to store the user's name, maximum length allowed is 100 characters
    name = models.CharField(max_length=100)
    # Field to store the user's email, must be a valid email format
    email = models.EmailField()
    # Field to store the user's password, maximum length allowed is 100 characters
    password = models.CharField(max_length=100)
    # Field to store the timestamp when the user record was created, automatically set to the current date and time when the user is created
    created_at = models.DateTimeField(auto_now_add=True)
    # Field to store the timestamp of the last update to the user record, automatically set to the current date and time whenever the user record is updated
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Note(models.Model):
    # Field to store the user's name, maximum length allowed is 100 characters
    title = models.CharField(max_length=100)
    # Field to store the user's email, must be a valid email format
    content = models.TextField()
    # Field to store the timestamp when the user record was created, automatically set to the current date and time when the user is created
    created_at = models.DateTimeField(auto_now_add=True)
    # Field to store the timestamp of the last update to the user record, automatically set to the current date and time whenever the user record is updated
    updated_at = models.DateTimeField(auto_now=True)
    # Field to store the user's email, must be a valid email format
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notes')

    def __str__(self):
        return self.title

