from django.db import models

# Create your models here.
class User(models.Model):
    class Meta(object):
        db_table = 'user'

    name = models.CharField(
        'Name', blank=False, null = False , max_length=255
    )


    email = models.CharField(
        'Email', blank=False, null=False, max_length=245
    )
    password = models.CharField(
        'Password', blank=False, null=False, max_length=200
    )
    token = models.CharField(
        'Token', blank=True, null=True,max_length=500 , db_index=True
    )
    token_expires = models.DateTimeField(
        "Token Expiration Date" ,blank=True, null=True
    )
    created_at = models.DateTimeField(
        "Creation date" ,blank=True, auto_now_add=True
    )
    updated_at = models.DateTimeField(
        "Updation time" ,blank=True, auto_now=True
    )
    
    