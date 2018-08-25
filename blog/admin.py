from django.contrib import admin

# Register your models here .
from blog.models import Post

class PostAdmin(admin.ModelAdmin):
    exclude = ['posted']
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Post, PostAdmin)
