

from django.db import models
import uuid

class User(models.Model):
    Name = models.CharField(max_length=20, blank=False, null=False)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, unique=True)
    Gender = models.CharField(max_length=20, default='')
    Dob = models.DateField(blank=True,  default='')
    profile_picture = models.CharField(max_length=200, default='', blank=True, null=True)
    Introduction_voice = models.CharField(max_length=200, default='', blank=True, null=True)
    Introduction_text = models.CharField(max_length=500, default='')
    Invitation_Code = models.IntegerField(null=True, blank=True)
    otp = models.CharField(max_length=8, null=True, blank=True)
    uid = models.CharField(max_length=50, null=True, blank=True)
    usertype = models.CharField(max_length=50, null=True, blank=True)
    token = models.CharField(max_length=300, null=True, blank=True)
    forget_password_token = models.CharField(max_length=100, null=True, blank=True)
    Otpcreated_at = models.DateTimeField(null=True, blank=True)
    Is_Approved= models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    coins = models.PositiveIntegerField(default=0) 
    def __str__(self):
        return str(self.Name)



class Follow(models.Model):
    user = models.ForeignKey(User, related_name='following', on_delete=models.CASCADE)
    following_user = models.ForeignKey(User, related_name='followers', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    
    def __str__(self):
        return self.user.Name
    



class Social_media(models.Model):
    Google = models.CharField(max_length=100, blank=True, null=True, unique=True)
    Facebook = models.CharField(max_length=100, blank=True, null=True, unique=True)
    Snapchat = models.CharField(max_length=100, blank=True, null=True, unique=True)
    def __str__(self):
        return str(self.Google)

class claim_coins(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    claim_coins = models.BooleanField(default=False)
    created_at = models.CharField(max_length=100)

    def __str__(self):
        return str(self.user)

class room_join_claim_coins(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    claim_coins = models.BooleanField(max_length=100)
    created_at = models.CharField(max_length=100)

    def __str__(self):
        return str(self.user)