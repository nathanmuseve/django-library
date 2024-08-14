from django.contrib import admin
from .models import Novel

##cutomized model
class NovelAdmin(admin.ModelAdmin):
  list_display = ('title','author','genre','description')
  
# Registered Models.
admin.site.register(Novel, NovelAdmin)