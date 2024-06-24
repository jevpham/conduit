from django.db import models
from django.contrib.auth.models import AbstractUser

# User model
# class User(AbstractUser):
class User(models.Model):
    # Field to store the user's name, maximum length allowed is 100 characters
    name = models.CharField(max_length=100)
    # Field to store the user's email, must be a valid email format, required on create
    email = models.EmailField(blank=False, null=False)
    # Field to store the user's password, maximum length allowed is 100 characters, required on create
    password = models.CharField(max_length=100, blank=False, null=False)

    # password = models.CharField(
    #     max_length=100, 
    #     blank=False, 
    #     null=False,
    #     validators=[
    #         MinLengthValidator(8),  # Minimum length of 8 characters
    #         RegexValidator(
    #             regex='^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$',
    #             message='Password must contain at least one uppercase letter, one lowercase letter, one number, and one special character.'
    #         )
    #     ]
    # )

    # Field to store the timestamp when the user record was created, automatically set to the current date and time when the user is created
    created_at = models.DateTimeField(auto_now_add=True)
    # Field to store the timestamp of the last update to the user record, automatically set to the current date and time whenever the user record is updated
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name