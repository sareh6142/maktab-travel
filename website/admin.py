from django.contrib import admin
from .models import Contact,Newsletter
# Register your models here.
class ContactAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    list_display = ('name','email','created_date',)
    list_filter = ('email','created_date')
    search_fields = ['name','message']

admin.site.register(Contact,ContactAdmin)
admin.site.register(Newsletter)