from django.contrib import admin
from .models import Notes, comment

class comment_admin(admin.StackedInline):
	model = comment

class notes_admin(admin.ModelAdmin):

	inlines = [comment_admin]
	class Meta:
		model = Notes

admin.site.register(Notes, notes_admin)
admin.site.register(comment)