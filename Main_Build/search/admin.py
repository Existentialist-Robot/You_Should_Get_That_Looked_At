from django.contrib import admin
from .models import People, Contact, Upload, Comment#Search

#class SearchAdmin(admin.ModelAdmin):
#    list_display = ('title','slug','author','date')
#    search_fields = ('title','body')
#    prepopulated_fields = {'slug': ('title',)}
#
#admin.site.register(Search, SearchAdmin)


class PeopleAdmin(admin.ModelAdmin):
    list_display = ('name','slug')
    search_fields = ('title','body')
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(People, PeopleAdmin)

class ContactAdmin(admin.ModelAdmin):
    list_display = ('name','from_email','date','receive_newsletter')
    list_fields = ('receive_newsletter')
    list_filter = ['receive_newsletter']
    search_fields = ['body']

admin.site.register(Contact, ContactAdmin)

class UploadAdmin(admin.ModelAdmin):
    list_display = ('title','slug','author')
    #list_display = ('title','slug','author','publish','status')
    # list_filter = ('status', 'author')
    search_fields = ('title','body')
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ('author',)

admin.site.register(Upload, UploadAdmin)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('upload','active','author')
    list_filter = ['active']
    search_fields = ('title','body')
    raw_id_fields = ('author',)

admin.site.register(Comment, CommentAdmin)
# admin.site.register(Comment)
