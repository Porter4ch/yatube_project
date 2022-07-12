from django.contrib import admin
from .models import Post
from .models import Group

class PostAdmin(admin.ModelAdmin):
    list_display = ('pk', 'text', 'pub_date', 'author') 
    search_fields = ('text',) 
    list_filter = ('pub_date',) 

admin.site.register(Post, PostAdmin)  

class GroupAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'description') 

admin.site.register(Group, GroupAdmin)