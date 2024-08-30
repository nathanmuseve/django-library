from django.contrib import admin
from .models import Novel, Person, Group, Membership

##cutomized model
class NovelAdmin(admin.ModelAdmin):
  list_display = ('title','author','genre','description')
  
# Registered Models.
admin.site.register(Novel, NovelAdmin)
admin.site.register(Person)
admin.site.register(Group)
admin.site.register(Membership)