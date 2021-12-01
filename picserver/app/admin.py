from django.contrib import admin

from .models import  Image,User,Chat,ChatImage,Tag



class  UserAdminModel(admin.ModelAdmin):
    list_display= ['userName','firstName','lastName','userEmail', 'userPermissions', 'userstatus']
    search_fields = ['userName', 'id']
    list_filter = ['userPermissions', 'country']
    
class ImageAdminModel(admin.ModelAdmin):
    list_display= ['imageTitle', 'id', 'user', 'imageDate']
    search_fields = ['imageTitle', 'id'] 
    list_filter = ['tags', 'user']  
    date_hierarchy = 'imageDate' 
class ChatAdminModel(admin.ModelAdmin):
    list_display = ['id']
    search_field = ['id']
class TagsAdminModel(admin.ModelAdmin):
    list_display = ['tagName']
    search_field = ['tagName']
# admin.site.register([Image,detailsAdmin,User,Chat,ChatImage])
admin.site.register(User, UserAdminModel)
admin.site.register(Image, ImageAdminModel)
admin.site.register(Chat, ChatAdminModel)
admin.site.register(Tag, TagsAdminModel)