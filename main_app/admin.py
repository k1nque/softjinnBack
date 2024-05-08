from django.contrib import admin

# Register your models here.

from main_app.models import wishes, wishes_to_implements

admin.site.register(wishes)
admin.site.register(wishes_to_implements)
# admin.site.register(users)
