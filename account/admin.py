from django.contrib import admin
from .models import User, Pothole, Corporator, Contractor, Allotment, Done

# Register your models here.
admin.site.register(User)
admin.site.register(Pothole)
admin.site.register(Corporator)
admin.site.register(Contractor)
admin.site.register(Allotment)
admin.site.register(Done)