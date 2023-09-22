from django.contrib import admin
from .models import User,Follow, Social_media

admin.site.register(User)
admin.site.register(Follow)
admin.site.register(Social_media)