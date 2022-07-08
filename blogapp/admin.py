from django.contrib import admin
from blogapp.models import Post, Plant, Comments


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status','created_on')
    list_filter = ("status",)
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Plant)
class PlantAdmin(admin.ModelAdmin):
    list_display = ('name', 'image')


@admin.register(Comments)
class CommentsAdmin(admin.ModelAdmin):
    list_display = ['author', 'posted', 'post']
