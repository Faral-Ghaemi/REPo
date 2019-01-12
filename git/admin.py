from django.contrib import admin
from . import models
# Register your models here.
class repositoryAdmin(admin.ModelAdmin):
    list_display = ('name','get_user_names')


admin.site.register(models.repository, repositoryAdmin)
