from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Customer)
admin.site.register(User)
admin.site.register(Account)
admin.site.register(Transaction)
admin.site.register(AccountChange)
admin.site.register(Report)
