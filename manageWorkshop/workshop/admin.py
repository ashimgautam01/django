from django.contrib import admin
from .models import Workshop,Member,Feedback,Post,Comment

class PostAdmin(admin.ModelAdmin):
    list_display=['title','created_At']

admin.site.register(Workshop)
admin.site.register(Member)
admin.site.register(Feedback)
admin.site.register(Post,PostAdmin)
admin.site.register(Comment)