from django.contrib import admin
from mess_app.models import Member
from mess_app.models import Meal
from mess_app.models import UserInfo

# Register your models here.
admin.site.register(Member)
admin.site.register(Meal)
admin.site.register(UserInfo)