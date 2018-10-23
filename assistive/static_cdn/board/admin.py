from django.contrib import admin

# Register your models here.
#from .models import Post
from .models import Board

class BoardModelAdmin(admin.ModelAdmin):
	list_display = ["title", "updated", "timestamp"]
	list_display_links = ["updated"]
	list_editable = ["title"]
	list_filter = ["updated", "timestamp"]

	search_fields = ["title", "content"]
	class Meta:
		model = Board


#admin.site.register(Post, PostModelAdmin)
#admin.site.register(Tag)
admin.site.register(Board,BoardModelAdmin)