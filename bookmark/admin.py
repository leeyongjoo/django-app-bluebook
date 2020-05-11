from django.contrib import admin

# Register your models here.
from bookmark.models import Bookmark

@admin.register(Bookmark) # admin.stie.register(Bookmark, BookmarkAdmin)
class BookmarkAdmin(admin.ModelAdmin):
	list_display = ('id', 'title', 'url')