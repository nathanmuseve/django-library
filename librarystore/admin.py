from django.contrib import admin
from .models import Novel, Person, Group, Membership,Contact

##cutomized model
class NovelAdmin(admin.ModelAdmin):
  list_display = ('title','author','genre','description')

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
  list_display = ('name', 'email', 'subscribe', 'submitted_at')

  
# Registered Models.
admin.site.register(Novel, NovelAdmin)
admin.site.register(Person)
admin.site.register(Group)
admin.site.register(Membership)