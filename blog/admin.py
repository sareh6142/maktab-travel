from django.contrib import admin
from .models import Post,Category
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.
class PostAdmin(SummernoteModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_display = '-empty-'
    list_display = ('title','counted_views', 'status','published_date',)
    list_filter = ('status',)
    ordering = ['-created_date']
    search_fields = ['title','content']
    summernote_fields = ('content',)

admin.site.register(Post,PostAdmin)

admin.site.register(Category)