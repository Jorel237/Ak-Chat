from django.contrib import admin
from .models import Features
from .models import posts
from .models import Room
from .models import Message

# Register your models here.
admin.site.register(Features)
admin.site.register(posts)
admin.site.register(Room)
admin.site.register(Message)